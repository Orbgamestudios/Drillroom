#!/usr/bin/env python3
import os
import sys

# Add paths
base_dir = "/home/cgslinde/DrillRoom/DrillRoom"
scratch_dir = os.path.join(base_dir, "scratch")
builder_dir = os.path.join(scratch_dir, "blueprint_builder")

sys.path.append(scratch_dir)
sys.path.append(builder_dir)

from test_map import covered_map
from cars_topics import CARS_TOPICS
from cp_topics import CP_TOPICS
from bb_topics import BB_TOPICS
from ps_topics import PS_TOPICS

output_path = os.path.join(base_dir, "MCAT-CURRICULUM-AND-TOPIC-TRACKER.md")

print(f"Loaded topics: CARS={len(CARS_TOPICS)}, CP={len(CP_TOPICS)}, BB={len(BB_TOPICS)}, PS={len(PS_TOPICS)}")
total_topics = len(CARS_TOPICS) + len(CP_TOPICS) + len(BB_TOPICS) + len(PS_TOPICS)
assert total_topics == 1000, f"Expected 1000 topics, got {total_topics}"
assert len(covered_map) == 131, f"Expected 131 covered topics, got {len(covered_map)}"

# Groupings
cars_categories = [
    ("Philosophy, Ethics & Epistemology", 1, 40),
    ("Art, Architecture, Aesthetics & Literary Theory", 41, 80),
    ("History, Historiography & Archaeology", 81, 120),
    ("Political Science, Law, Jurisprudence & Government", 121, 160),
    ("Sociology, Anthropology & Cultural Studies", 161, 200),
]

cp_categories = [
    ("Translational Motion, Forces, Work & Energy", 201, 245),
    ("Fluids, Hydrostatics & Hemodynamics", 246, 280),
    ("Electrostatics, Circuits & Electromagnetism", 281, 325),
    ("Periodic Trends, Bonding, Chemical Reactions & Stoichiometry", 326, 365),
    ("Thermodynamics, Kinetics & Equilibrium", 366, 400),
    ("Waves, Sound & Optics", 401, 435),
    ("Organic Chemistry Structure, Mechanisms & Spectroscopy", 436, 470),
]

bb_categories = [
    ("Amino Acids, Peptides & Protein Chemistry", 471, 515),
    ("Enzymes, Kinetics, Allosterism & Catalytic Mechanisms", 516, 550),
    ("Metabolism, Bioenergetics, Carbohydrates & Lipids", 551, 605),
    ("Molecular Biology, Genetics, DNA Replication & Repair", 606, 650),
    ("Cell Biology, Organelles, Membrane Transport & Microbiology", 651, 695),
    ("Organ Systems Physiology & Developmental Biology", 696, 740),
]

ps_categories = [
    ("Sensory Processing, Perception & Psychophysics", 741, 785),
    ("Cognition, Memory, Consciousness & Language", 786, 855),
    ("Learning, Conditioning, Motivation & Emotion", 856, 895),
    ("Developmental Psychology & Personality Theories", 896, 930),
    ("Psychological Disorders, Neuropathology & Treatment", 931, 960),
    ("Social Processes, Interpersonal Interaction, Culture & Stratification", 961, 1000),
]

def format_topic(topic_tuple):
    num, title, focus = topic_tuple
    if num in covered_map:
        source = covered_map[num]
        return f"- [x] **{num}. {title}** — `{source}`  \n  *High-Yield Focus:* {focus}\n"
    else:
        return f"- [ ] **{num}. {title}**  \n  *High-Yield Focus:* {focus}\n"

with open(output_path, "w", encoding="utf-8") as f:
    # Title & Introduction
    f.write("# MCAT Master Curriculum & 1,000-Topic Coverage Tracker\n\n")
    f.write("A definitive, granular audit of all created content in **DrillRoom**, mapped against the official AAMC Foundational Concepts and past exam topic blueprints, expanded to an exhaustive **1,000-topic master curriculum**.\n\n")
    f.write("> **Purpose:** Use this document to track content coverage across CARS, C/P, B/B, and P/S. Before generating new 90-minute exams, 60-minute exams, or targeted drill modules, consult this tracker to select unchecked `[ ]` topics. Once implemented, mark them as checked `[x]` and cite the file and passage/discrete set ID to ensure zero duplication, rigorous topic breadth, and comprehensive coverage across the entire MCAT syllabus.\n\n")
    f.write("---\n\n")

    # Content Coverage Dashboard
    f.write("## 📊 Content Coverage Dashboard\n\n")
    f.write("| Section | Total Blueprint Topics | Created & Integrated `[x]` | Remaining Uncovered `[ ]` | Coverage % |\n")
    f.write("| :--- | :---: | :---: | :---: | :---: |\n")
    f.write("| **CARS** (Critical Analysis & Reasoning) | 200 | 30 | 170 | **15.0%** |\n")
    f.write("| **C/P** (Chemical & Physical Foundations) | 270 | 33 | 237 | **12.2%** |\n")
    f.write("| **B/B** (Biological & Biochemical Foundations) | 270 | 35 | 235 | **13.0%** |\n")
    f.write("| **P/S** (Psychological, Social & Biological) | 260 | 33 | 227 | **12.7%** |\n")
    f.write("| **TOTALS** | **1,000** | **131** | **869** | **13.1%** |\n\n")
    f.write("---\n\n")

    # Audit of Currently Created Content
    f.write("## 🔍 Audit of Currently Created Content in DrillRoom (131 Covered Sets)\n\n")

    # CARS Audit
    f.write("### 1. CARS Existing Passages (30 Passages / Sets)\n")
    f.write("#### Exam 1 Suite & Base Drill Sets (21 Passages)\n")
    for num in range(1, 22):
        title = [t[1] for t in CARS_TOPICS if t[0] == num][0]
        source = covered_map[num]
        f.write(f"* `{source}`: **{title}**\n")
    f.write("\n#### Exam 2 Suite (9 Passages)\n")
    for num in range(22, 31):
        title = [t[1] for t in CARS_TOPICS if t[0] == num][0]
        source = covered_map[num]
        f.write(f"* `{source}`: **{title}**\n")
    f.write("\n---\n\n")

    # C/P Audit
    f.write("### 2. C/P Existing Topics (33 Topics / Sets)\n")
    f.write("#### Exam 1 Suite & Base Drill Sets (16 Topics)\n")
    for num in range(201, 217):
        title = [t[1] for t in CP_TOPICS if t[0] == num][0]
        source = covered_map[num]
        f.write(f"* `{source}`: **{title}**\n")
    f.write("\n#### Exam 2 Suite (17 Topics)\n")
    for num in range(217, 234):
        title = [t[1] for t in CP_TOPICS if t[0] == num][0]
        source = covered_map[num]
        f.write(f"* `{source}`: **{title}**\n")
    f.write("\n---\n\n")

    # B/B Audit
    f.write("### 3. B/B Existing Topics (35 Topics / Sets)\n")
    f.write("#### Exam 1 Suite & Base Drill Sets (20 Topics)\n")
    for num in range(471, 491):
        title = [t[1] for t in BB_TOPICS if t[0] == num][0]
        source = covered_map[num]
        f.write(f"* `{source}`: **{title}**\n")
    f.write("\n#### Exam 2 Suite (15 Topics)\n")
    for num in range(491, 506):
        title = [t[1] for t in BB_TOPICS if t[0] == num][0]
        source = covered_map[num]
        f.write(f"* `{source}`: **{title}**\n")
    f.write("\n---\n\n")

    # P/S Audit
    f.write("### 4. P/S Existing Topics (33 Topics / Sets)\n")
    f.write("#### Exam 1 Suite & Base Drill Sets (19 Topics)\n")
    for num in range(741, 760):
        title = [t[1] for t in PS_TOPICS if t[0] == num][0]
        source = covered_map[num]
        f.write(f"* `{source}`: **{title}**\n")
    f.write("\n#### Exam 2 Suite (14 Topics)\n")
    for num in range(760, 774):
        title = [t[1] for t in PS_TOPICS if t[0] == num][0]
        source = covered_map[num]
        f.write(f"* `{source}`: **{title}**\n")
    f.write("\n---\n\n")

    # Section I: CARS
    f.write("## Section I: Critical Analysis & Reasoning Skills (CARS)\n")
    f.write("### 200 Topics Across Humanities & Social Sciences\n\n")
    cars_dict = {t[0]: t for t in CARS_TOPICS}
    for cat_name, start_idx, end_idx in cars_categories:
        f.write(f"### {cat_name} (Topics {start_idx} - {end_idx})\n\n")
        for num in range(start_idx, end_idx + 1):
            if num in cars_dict:
                f.write(format_topic(cars_dict[num]))
        f.write("\n")
    f.write("---\n\n")

    # Section II: C/P
    f.write("## Section II: Chemical & Physical Foundations of Biological Systems (C/P)\n")
    f.write("### 270 Topics Across Physics, General Chemistry & Organic Chemistry\n\n")
    cp_dict = {t[0]: t for t in CP_TOPICS}
    for cat_name, start_idx, end_idx in cp_categories:
        f.write(f"### {cat_name} (Topics {start_idx} - {end_idx})\n\n")
        for num in range(start_idx, end_idx + 1):
            if num in cp_dict:
                f.write(format_topic(cp_dict[num]))
        f.write("\n")
    f.write("---\n\n")

    # Section III: B/B
    f.write("## Section III: Biological & Biochemical Foundations of Living Systems (B/B)\n")
    f.write("### 270 Topics Across Biochemistry, Molecular Biology, Cell Biology & Physiology\n\n")
    bb_dict = {t[0]: t for t in BB_TOPICS}
    for cat_name, start_idx, end_idx in bb_categories:
        f.write(f"### {cat_name} (Topics {start_idx} - {end_idx})\n\n")
        for num in range(start_idx, end_idx + 1):
            if num in bb_dict:
                f.write(format_topic(bb_dict[num]))
        f.write("\n")
    f.write("---\n\n")

    # Section IV: P/S
    f.write("## Section IV: Psychological, Social & Biological Foundations of Behavior (P/S)\n")
    f.write("### 260 Topics Across Psychology, Sociology, Biological Bases & Social Stratification\n\n")
    ps_dict = {t[0]: t for t in PS_TOPICS}
    for cat_name, start_idx, end_idx in ps_categories:
        f.write(f"### {cat_name} (Topics {start_idx} - {end_idx})\n\n")
        for num in range(start_idx, end_idx + 1):
            if num in ps_dict:
                f.write(format_topic(ps_dict[num]))
        f.write("\n")

print(f"Successfully assembled and wrote 1,000-topic tracker to {output_path}")
