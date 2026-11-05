with open('/home/cgslinde/DrillRoom/DrillRoom/gemini_analysis.js') as f:
    content = f.read()

# Replace DEFAULT_MODEL and SUPPORTED_MODELS
old_models = """  const DEFAULT_MODEL = "gemini-2.5-flash";
  const SUPPORTED_MODELS = [
    { id: "gemini-2.5-flash", name: "Gemini 2.5 Flash (Recommended - Fast & Smart)" },
    { id: "gemini-2.0-flash", name: "Gemini 2.0 Flash (Next-Gen Flash)" },
    { id: "gemini-1.5-flash", name: "Gemini 1.5 Flash (Standard Flash)" },
    { id: "gemini-1.5-pro",   name: "Gemini 1.5 Pro (Deep Cognitive Reasoning)" }
  ];"""

new_models = """  const DEFAULT_MODEL = "gemini-3.8-flash";
  const SUPPORTED_MODELS = [
    { id: "gemini-3.8-flash", name: "Gemini 3.8 Flash (Newest Flagship — Fast & Advanced)" },
    { id: "gemini-3.8-pro",   name: "Gemini 3.8 Pro (Maximum Cognitive Reasoning)" },
    { id: "gemini-3.8",       name: "Gemini 3.8 (Base)" },
    { id: "gemini-2.5-flash", name: "Gemini 2.5 Flash" },
    { id: "gemini-2.0-flash", name: "Gemini 2.0 Flash" },
    { id: "gemini-1.5-flash", name: "Gemini 1.5 Flash" },
    { id: "gemini-1.5-pro",   name: "Gemini 1.5 Pro" }
  ];

  /* Fetch all available models accessible with this API key */
  async function fetchAvailableModels(apiKey) {
    if (!apiKey) return [];
    try {
      const res = await fetch(`https://generativelanguage.googleapis.com/v1beta/models?key=${encodeURIComponent(apiKey)}`);
      if (!res.ok) return [];
      const data = await res.json();
      if (!data.models || !Array.isArray(data.models)) return [];
      return data.models
        .filter(m => m.supportedGenerationMethods && m.supportedGenerationMethods.includes("generateContent"))
        .map(m => {
          const id = m.name.replace(/^models\//, "");
          return { id, name: m.displayName ? `${m.displayName} (${id})` : id };
        });
    } catch (e) {
      return [];
    }
  }"""

assert old_models in content, "old_models not found in content"
content = content.replace(old_models, new_models)

# Update modelsToTry in callGeminiAPI
old_caller = """    const modelsToTry = [
      requestedModel || getModel(),
      "gemini-2.5-flash",
      "gemini-2.0-flash",
      "gemini-1.5-flash",
      "gemini-1.5-pro"
    ].filter((v, i, a) => a.indexOf(v) === i);"""

new_caller = """    const cleanModel = (requestedModel || getModel()).replace(/^models\//, "").trim();
    const modelsToTry = [
      cleanModel,
      "gemini-3.8-flash",
      "gemini-3.8-pro",
      "gemini-3.8",
      "gemini-2.5-flash",
      "gemini-2.0-flash",
      "gemini-1.5-flash",
      "gemini-1.5-pro"
    ].filter((v, i, a) => v && a.indexOf(v) === i);"""

assert old_caller in content, "old_caller not found in content"
content = content.replace(old_caller, new_caller)

# Update card options generation
old_card_select = """          <select id="gCardModelSelect" style="padding:7px 10px;border:1px solid var(--line);border-radius:2px;font-size:12.5px;background:#fff">
            ${SUPPORTED_MODELS.map(m => `<option value="${m.id}" ${m.id === currentModel ? "selected" : ""}>${m.name}</option>`).join("")}
          </select>"""

new_card_select = """          <select id="gCardModelSelect" style="padding:7px 10px;border:1px solid var(--line);border-radius:2px;font-size:12.5px;background:#fff">
            ${(!SUPPORTED_MODELS.some(m => m.id === currentModel) ? `<option value="${escapeHtml(currentModel)}" selected>${escapeHtml(currentModel)} (Custom)</option>` : "")}
            ${SUPPORTED_MODELS.map(m => `<option value="${m.id}" ${m.id === currentModel ? "selected" : ""}>${m.name}</option>`).join("")}
          </select>"""

assert old_card_select in content, "old_card_select not found"
content = content.replace(old_card_select, new_card_select)

with open('/home/cgslinde/DrillRoom/DrillRoom/gemini_analysis.js', 'w') as f:
    f.write(content)

print("gemini_analysis.js base models updated successfully!")
