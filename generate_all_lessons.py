import json

# استرجاع الدروس الحالية واضافة A2 و B1
with open('lessons_a1.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

a2_b1_lessons = [
    # دروس A2
    {
        "id": 11,
        "title": "Reflexive Verben",
        "title_ar": "الأفعال المنعكسة",
        "level": "A2",
        "explanation": "الأفعال التي ينعكس أثرها على الفاعل وتأخذ الضمير المنعكس mich/dich/sich.",
        "examples": [{"de": "Ich wasche mich.", "ar": "أنا أغسل نفسي."}],
        "quiz": [{"question": "Du wäschst ____.", "options": ["dich", "mich", "sich", "euch"], "answer": "dich"}]
    },
    {
        "id": 12,
        "title": "Nebensätze mit weil und dass",
        "title_ar": "الجمل الجانبية مع لأن وأن",
        "level": "A2",
        "explanation": "الروابط weil و dass ترسل الفعل المصرف مباشرة إلى نهاية الجملة.",
        "examples": [{"de": "Ich lerne, weil ich Deutsch brauche.", "ar": "أتعلم لأنني أحتاج الألمانية."}],
        "quiz": [{"question": "Er sagt, dass er Zeit ____.", "options": ["hat", "hast", "haben", "hatte"], "answer": "hat"}]
    },
    # دروس B1
    {
        "id": 13,
        "title": "Passiv (المبني للمجهول)",
        "title_ar": "صياغة المبني للمجهول",
        "level": "B1",
        "explanation": "يتكون من فعل werden المصرف + Partizip II في نهاية الجملة التركيز على الفعل لا الفاعل.",
        "examples": [{"de": "Das Auto wird repariert.", "ar": "السيارة تُصلَح."}],
        "quiz": [{"question": "Das Haus ____ gebaut.", "options": ["wird", "werden", "wurden", "ist"], "answer": "wird"}]
    },
    {
        "id": 14,
        "title": "Konjunktiv II (صيغة التمني والافتراض)",
        "title_ar": "التعبير عن الأمني والطلب الأدبي",
        "level": "B1",
        "explanation": "نستخدم würde + Infinitiv أو wäre/hätte للتعبير عن الأفكار الخيالية والطلب المهذب.",
        "examples": [{"de": "Ich würde gerne reisen.", "ar": "أود السفر بحب."}],
        "quiz": [{"question": "Ich ____ gerne einen Kaffee.", "options": ["hätte", "habe", "bin", "wäre"], "answer": "hätte"}]
    }
]

lessons.extend(a2_b1_lessons)

with open('all_lessons.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, ensure_ascii=False, indent=2)

print(f"✅ تم دمج وتحديث المنهج الكامل! إجمالي الدروس: {len(lessons)}")
