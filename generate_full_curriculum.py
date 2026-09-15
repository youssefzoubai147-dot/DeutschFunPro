import json

# بناء 15 درساً لمستوى A1
a1_lessons = [
    {"id": 1, "title": "Alphabet und Aussprache", "title_ar": "الأبجدية ونطق الحروف المركبة", "level": "A1"},
    {"id": 2, "title": "Personalpronomen", "title_ar": "الضمائر الشخصية وتصريف الأفعال العادية", "level": "A1"},
    {"id": 3, "title": "Bestimmter Artikel", "title_ar": "أدوات التعريف (der, die, das)", "level": "A1"},
    {"id": 4, "title": "Unbestimmter & Negativartikel", "title_ar": "أدوات النكرة والنفي (ein, kein)", "level": "A1"},
    {"id": 5, "title": "Verb sein und haben", "title_ar": "تصريف أفعال الكينونة والملكية", "level": "A1"},
    {"id": 6, "title": "W-Fragen und Ja/Nein-Fragen", "title_ar": "صياغة الأسئلة المباشرة وغير المباشرة", "level": "A1"},
    {"id": 7, "title": "Pluralformen", "title_ar": "قواعد وقوانين جمع الأسماء", "level": "A1"},
    {"id": 8, "title": "Akkusativ Kasus", "title_ar": "حالة النصب والمفعول به", "level": "A1"},
    {"id": 9, "title": "Modalverben (können, müssen)", "title_ar": "الأفعال الناقصة الجزء الأول", "level": "A1"},
    {"id": 10, "title": "Modalverben (wollen, möchten)", "title_ar": "الأفعال الناقصة الجزء الثاني", "level": "A1"},
    {"id": 11, "title": "Possessivartikel", "title_ar": "أدوات الملكية (mein, dein...)", "level": "A1"},
    {"id": 12, "title": "Imperativ", "title_ar": "صيغة الأمر والتوجيهات", "level": "A1"},
    {"id": 13, "title": "Präpositionen mit Akkusativ", "title_ar": "حروف الجر مع حالة النصب", "level": "A1"},
    {"id": 14, "title": "Zahlen und Uhrzeit", "title_ar": "الأرقام وقراءة الساعة والتاريخ", "level": "A1"},
    {"id": 15, "title": "Perfekt Grundlagen", "title_ar": "مقدمة للماضي التام مع haben", "level": "A1"}
]

# بناء 15 درساً لمستوى A2
a2_lessons = [
    {"id": 16, "title": "Dativ Kasus", "title_ar": "حالة المجرور Dativ", "level": "A2"},
    {"id": 17, "title": "Präpositionen mit Dativ", "title_ar": "حروف الجر التي تأخذ Dativ دائماً", "level": "A2"},
    {"id": 18, "title": "Wechselpräpositionen", "title_ar": "حروف الجر المشتركة بين Dativ و Akkusativ", "level": "A2"},
    {"id": 19, "title": "Trennbare und Untrennbare Verben", "title_ar": "الأفعال المنفصلة وغير المنفصلة", "level": "A2"},
    {"id": 20, "title": "Perfekt mit sein", "title_ar": "الماضي التام مع أفعال الحركة (sein)", "level": "A2"},
    {"id": 21, "title": "Präteritum (war, hatte)", "title_ar": "الماضي البسيط للأفعال المساعدة", "level": "A2"},
    {"id": 22, "title": "Reflexive Verben", "title_ar": "الأفعال المنعكسة وضمائرها", "level": "A2"},
    {"id": 23, "title": "Nebensätze (weil, dass)", "title_ar": "الجمل الجانبية مع لأن وأن", "level": "A2"},
    {"id": 24, "title": "Nebensätze (wenn, ob)", "title_ar": "الجمل الشرطية وأسئلة الشك", "level": "A2"},
    {"id": 25, "title": "Komparativ und Superlativ", "title_ar": "درجات المقارنة والتفضيل للمقارنات", "level": "A2"},
    {"id": 26, "title": "Adjektivdeklination (Bestimmt)", "title_ar": "إعراب الصفات بعد أدوات التعريف", "level": "A2"},
    {"id": 27, "title": "Adjektivdeklination (Unbestimmt)", "title_ar": "إعراب الصفات بعد أدوات النكرة", "level": "A2"},
    {"id": 28, "title": "Verben mit Dativ und Akkusativ", "title_ar": "أفعال تاخذ مفعولين (مجرور ونصب)", "level": "A2"},
    {"id": 29, "title": "Demonstrativpronomen", "title_ar": "أسماء الإشارة (dieser, jede...)", "level": "A2"},
    {"id": 30, "title": "Infinitiv mit zu", "title_ar": "المصدر مع zu والجمل التوضيحية", "level": "A2"}
]

# بناء 15 درساً لمستوى B1
b1_lessons = [
    {"id": 31, "title": "Passiv Präsens", "title_ar": "المبني للمجهول في الحاضر", "level": "B1"},
    {"id": 32, "title": "Passiv Präteritum", "title_ar": "المبني للمجهول في الماضي البسيط", "level": "B1"},
    {"id": 33, "title": "Konjunktiv II (Wünsche)", "title_ar": "صيغة التمني والافتراض المتقدمة", "level": "B1"},
    {"id": 34, "title": "Konjunktiv II (Höflichkeit)", "title_ar": "استخدامات الطلب المهذب جداً", "level": "B1"},
    {"id": 35, "title": "Genitiv Kasus", "title_ar": "حالة المضاف إليه Genitiv وقواعدها", "level": "B1"},
    {"id": 36, "title": "Präpositionen mit Genitiv", "title_ar": "حروف الجر المتقدمة مع المضاف إليه (wegen, trotz)", "level": "B1"},
    {"id": 37, "title": "Relativsätze im Nominativ & Akkusativ", "title_ar": "جمل الوصل في الرفع والنصب", "level": "B1"},
    {"id": 38, "title": "Relativsätze im Dativ & Genitiv", "title_ar": "جمل الوصل في المجرور والمضاف إليه", "level": "B1"},
    {"id": 39, "title": "N-Deklination", "title_ar": "إعراب الأسماء الضعيفة المذكرة", "level": "B1"},
    {"id": 40, "title": "Zweiteilige Konnektoren", "title_ar": "الروابط المزدوجة (zwar... aber, sowohl... als auch)", "level": "B1"},
    {"id": 41, "title": "Partizip I und II als Adjektiv", "title_ar": "تحويل اسم الفاعل والمفعول إلى صفات", "level": "B1"},
    {"id": 42, "title": "Futur I", "title_ar": "زمن المستقبل والتعبير عن التوقعات", "level": "B1"},
    {"id": 43, "title": "Verben mit Präpositionen", "title_ar": "الأفعال المرتبطة بحروف جر ثابتة", "level": "B1"},
    {"id": 44, "title": "Pronominaladverbien (dafür, worüber)", "title_ar": "الضمائر الظرفية والاستفهامية", "level": "B1"},
    {"id": 45, "title": "Plusquamperfekt", "title_ar": "الماضي الأسبق والتتابع الزمني للأحداث", "level": "B1"}
]

full_curriculum = []
for lesson in a1_lessons + a2_lessons + b1_lessons:
    full_curriculum.append({
        "id": lesson["id"],
        "title": lesson["title"],
        "title_ar": lesson["title_ar"],
        "level": lesson["level"],
        "explanation": f"شرح تفصيلي وقواعد درس {lesson['title_ar']} لمستوى {lesson['level']}.",
        "examples": [{"de": f"Beispiel für {lesson['title']}.", "ar": f"مثال توضيحي لدرس {lesson['title_ar']}."}],
        "quiz": [{"question": f"Frage zu {lesson['title']}?", "options": ["Option A", "Option B"], "answer": "Option A"}]
    })

with open('all_lessons.json', 'w', encoding='utf-8') as f:
    json.dump(full_curriculum, f, ensure_ascii=False, indent=2)

print(f"✅ تم توليد المنهاج الشامل بنجاح! الإجمالي: {len(full_curriculum)} درساً.")
