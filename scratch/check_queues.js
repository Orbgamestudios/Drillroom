const fs = require('fs');
const vm = require('vm');
const path = require('path');
const dir = '/home/cgslinde/DrillRoom/DrillRoom';

const dummyElem = {
    onclick: null,
    addEventListener: () => {},
    style: {},
    classList: { add: () => {}, remove: () => {}, contains: () => false },
    innerHTML: '',
    appendChild: () => {},
};

const sandbox = {
    console: console,
    $: (id) => dummyElem,
    document: {
        getElementById: (id) => dummyElem,
        querySelector: (sel) => dummyElem,
        querySelectorAll: (sel) => [],
        createElement: (tag) => dummyElem,
        addEventListener: () => {},
        body: dummyElem,
    },
    localStorage: {
        getItem: () => null,
        setItem: () => {},
        removeItem: () => {},
    },
};
sandbox.window = sandbox;
sandbox.global = sandbox;
const context = vm.createContext(sandbox);

const html = fs.readFileSync(path.join(dir, 'DrillRoom.html'), 'utf8');
const scriptMatches = [...html.matchAll(/<script src=["'](.*?)["']><\/script>/g)].map(m => m[1]);
for (const scriptFile of scriptMatches) {
    if (scriptFile === 'gemini_analysis.js') continue;
    const filePath = path.join(dir, scriptFile);
    const code = fs.readFileSync(filePath, 'utf8');
    vm.runInContext(code, context, { filename: scriptFile });
}
sandbox.autoRegisterExams();

const exams = sandbox.PRACTICE_EXAMS;
const subjects = ['C/P', 'CARS', 'B/B', 'P/S'];
const durations = [90, 60];

console.log('=== QUEUE ORDER CHECK ===');
for (const sec of subjects) {
    for (const dur of durations) {
        const queue = exams.filter(e => e.sec === sec && e.duration === dur);
        queue.sort((a,b) => (a.suite || '').localeCompare(b.suite || '', undefined, { numeric: true }));
        const ids = queue.map(e => e.id).join(' -> ');
        console.log(`[${sec} ${dur}m] (${queue.length} exams): ${ids}`);
    }
}
