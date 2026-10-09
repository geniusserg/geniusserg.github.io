#!/usr/bin/env python3
import base64, html

def esc(s):
    return html.escape(s, quote=False)

photo = base64.b64encode(open('/tmp/cv_deploy/Data/image1-31.png', 'rb').read()).decode()

def icon_b64(path):
    return base64.b64encode(open(path, 'rb').read()).decode()

company_icons = {
    'huawei': icon_b64('/tmp/cv_deploy/icons/huawei.com.png'),
    'itmo': icon_b64('/tmp/cv_deploy/icons/itmo.ru.png'),
    'harman': icon_b64('/tmp/cv_deploy/icons/harman.com.png'),
    'intel': icon_b64('/tmp/cv_deploy/icons/intel.com.png'),
    'hse': icon_b64('/tmp/cv_deploy/icons/hse.ru.png'),
}

def icon_for(key):
    if key and key in company_icons:
        return f'<img class="cicon" src="data:image/png;base64,{company_icons[key]}" alt="">'
    return ''

BTN_SVG = {
    'tg': '<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor" aria-hidden="true"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>',
    'mail': '<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor" aria-hidden="true"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>',
    'in': '<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor" aria-hidden="true"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.225 0z"/></svg>',
}

YT_ICON = '<svg viewBox="0 0 24 24" width="12" height="12" fill="currentColor" aria-hidden="true"><path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.5 12 3.5 12 3.5s-7.5 0-9.4.6A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.6 9.4.6 9.4.6s7.5 0 9.4-.6a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.6 15.6V8.4L15.8 12z"/></svg>'

I18N = {
    'en': {
        'name': 'Danilov Sergey Dmitrievich',
        'location': 'Saint Petersburg, Russia',
        'title': 'Danilov Sergey Dmitrievich — Resume',
        'footer': 'Danilov Sergey Dmitrievich · Resume',
        'download': '⬇ Download PDF',
        'like': 'Like',
        'liked': 'Liked',
        'views': 'views',
        'doc': '📄 doc',
        'summary': ("ML/LLMOps Engineer who owns the full lifecycle of production ML and LLM serving — "
                    "model deployment, distributed inference, GPU orchestration, vLLM and VeRL, batching and scheduling, "
                    "MoE routing, and predictive reliability of cluster hardware (memory, network) — turning models into "
                    "reliable, high-availability services with measurable SLO."),
        'sections': [
            ("Career", [
                ('job', 'huawei', "Huawei — LLM Inference R&D Engineer", "September 2024 – present", [
                    "Disaggregated Prefill/Decode simulator — C++ discrete-event simulation of a prefill/decode serving system with KV-cache-aware load balancing and Markov request traffic; selects TP/DP/SP/EP topology and scheduling policy to hold 99.99% SLO, and steers vLLM recovery for RL rollouts.",
                    "Time-series clustering of optical-power telemetry flags degrading links early; a minimal-parameter model that raised cluster availability by +10%.",
                    ("NUMA-aware stress testing reached 95% of theoretical bandwidth; Weibull MTTR modeling + XGBoost failure forecasting cut repair costs by 2×.", "https://support.huaweicloud.com/intl/en-us/usermanual-server-modelarts/usermanual-server-0036.html#section11"),
                    "Combinatorial EPLB MoE expert-placement algorithms that co-optimize expert-to-GPU mapping with all-to-all communication to minimize network congestion and tail latency.",
                    "Deep knowledge across the serving stack: continuous batching and preemptive scheduling, fused communication operators, FP8/INT8 quantization, speculative decoding, and optimization trade-offs.",
                ]),
                ('job', 'itmo', "ML Engineer — ITMO University", "November 2023 – September 2024", [
                    "Sber & ITMO: CTGAN user emulator; improved BiVAE recommendation MAP@5 by 3%.",
                    "Almazov & ITMO: Shapley-valued weighted XGBoost for obesity treatment; 71% accuracy for 3-month sibutramine therapy response; 2 Q2 papers.",
                    "Industrial AI assistant: improved PDF NER with prompt engineering/self-consistency; filtering removed 80% repetition.",
                ]),
                ('job', 'harman', "Testing Engineer — Harman", "September 2021 – July 2022", [
                    "Sped up testing for complex GPS automotive systems with Robot Framework",
                ]),
                ('job', 'intel', "Release Engineer — Intel", "July 2019 – August 2021", [
                    "Supported Intel OneAPI HPC release infrastructure: Python/Bash automation and C++ installer.",
                ]),
            ]),
            ("Tech Stack", [
                ('bullet', "AI infrastructure: Harness, Agents workflow, RAG, CAG, vLLM, VeRL, PyTorch, Kubernetes", None),
                ('bullet', "Data Analysis & Research: Python, Pandas, Scikit-learn, AutoML, PatentScope, Elsevier Scopus", None),
            ]),
            ("Education", [
                ('entry', 'itmo', "ITMO University, 2024 — Master's degree in Data Analysis", None, [
                    "Thesis: Shapley-value weighted filtering for small-sample ML; +7% accuracy on medical data.",
                ]),
                ('entry', 'hse', "Higher School of Economics, 2022 — Bachelor's degree in Software Engineering", None, [
                    "Thesis: accessible assistant for visually impaired users using Yandex Cloud OCR.",
                ]),
            ]),
            ("Publications", [
                ('bullet', "Google Scholar · h-index 2", "https://scholar.google.com/citations?user=sD1qs3QAAAAJ"),
                ('bullet', "Danilov et al., J. Pers. Med. 2024, 14, 811 — sibutramine therapy prediction.", "https://doi.org/10.3390/jpm14080811"),
                ('bullet', "Markina et al., J. Clin. Med. 2024, 13, 4151 — brown adipose tissue and obesity treatment.", "https://doi.org/10.3390/jcm13144151"),
            ]),
            ("Competitions", [
                ('entry', None, "ScienceRAG — Research assistant agent based on GigaChat", None, [
                    ("ScienceRAG: improved ArXiv RAG retrieval on GigaChat", "https://youtu.be/ri2OOypFLXc?t=11214", 'yt'),
                ]),
                ('entry', None, "X5 AI Tech Hackathon — Hallucination detection algorithm", None, [
                    ("X5 AI Tech: ruBERT hallucination detector — 88% accuracy, <0.45 s inference; top-10.", "https://codenrock.com/users/79846/certificates/250"),
                ]),
            ]),
            ("Languages", [
                ('bullet', "Russian, English (B1)", None),
            ]),
        ],
    },
    'ru': {
        'name': 'Данилов Сергей Дмитриевич',
        'location': 'Санкт-Петербург, Россия',
        'title': 'Данилов Сергей Дмитриевич — Резюме',
        'footer': 'Данилов Сергей Дмитриевич · Резюме',
        'download': '⬇ Скачать PDF',
        'like': 'Нравится',
        'liked': 'Спасибо',
        'views': 'просмотров',
        'doc': '📄 документация',
        'summary': ("ML/LLMOps-инженер, который владеет полным циклом эксплуатации ML и LLM в продакшене — "
                    "деплой моделей, распределённый инференс, оркестрация GPU, vLLM и VeRL, батчинг и планирование, "
                    "MoE-маршрутизация и прогнозирование отказов кластерного оборудования (память, сеть) — "
                    "и превращает модели в надёжные высокодоступные сервисы с измеримым SLO."),
        'sections': [
            ("Опыт работы", [
                ('job', 'huawei', "Huawei — R&D-инженер по LLM-инференсу", "Сентябрь 2024 – настоящее время", [
                    "Симулятор disaggregated Prefill/Decode — дискретно-событийное моделирование на C++ системы prefill/decode-обслуживания с балансировкой нагрузки с учётом KV-кэша и марковским трафиком запросов; выбор топологии TP/DP/SP/EP и политики планирования для удержания SLO 99,99%; восстановление vLLM для RL-прогонов.",
                    "Кластеризация временных рядов телеметрии оптической мощности заранее выявляет деградирующие каналы; модель с минимальным числом параметров повысила доступность кластера на +10%.",
                    ("NUMA-осознанное стресс-тестирование достигло 95% теоретической пропускной способности; моделирование MTTR (распределение Вейбулла) + прогнозирование отказов (XGBoost) благодаря раннему предупреждению снизили издержки от ошибок памяти в big data приложениях в два раза.", "https://support.huaweicloud.com/intl/en-us/usermanual-server-modelarts/usermanual-server-0036.html#section11"),
                    "Комбинаторные алгоритмы размещения экспертов MoE (EPLB), совместно оптимизирующие маппинг «эксперт → GPU» и all-to-all-коммуникации, чтобы минимизировать перегрузку сети и хвостовую задержку.",
                    "Глубокое знание стека обслуживания: continuous batching и вытесняющее планирование, fused-коммуникации, квантизация FP8/INT8, спекулятивное декодирование и trade-off оптимизации.",
                ]),
                ('job', 'itmo', "ML-инженер — Университет ИТМО", "Ноябрь 2023 – Сентябрь 2024", [
                    "Сбер и ИТМО: эмулятор пользователей на CTGAN; улучшил MAP@5 рекомендательной системы BiVAE на 3%.",
                    "Алмазова и ИТМО: взвешенный XGBoost с весами Шепли для лечения ожирения; точность 71% в прогнозе ответа на терапию сибутрамином за 3 месяца; 2 статьи Q2.",
                    "Промышленный ИИ-ассистент: улучшил NER по PDF с помощью prompt engineering/self-consistency; фильтрация убрала 80% повторов.",
                ]),
                ('job', 'harman', "Инженер по тестированию — Harman", "Сентябрь 2021 – Июль 2022", [
                    "Ускорил тестирование сложных автомобильных GPS-систем с помощью Robot Framework",
                ]),
                ('job', 'intel', "Release-инженер — Intel", "Июль 2019 – Август 2021", [
                    "Поддерживал release-инфраструктуру Intel OneAPI HPC: автоматизация на Python/Bash и инсталлятор на C++.",
                ]),
            ]),
            ("Технологии", [
                ('bullet', "AI-инфраструктура: Harness, Agents workflow, RAG, CAG, vLLM, VeRL, PyTorch, Kubernetes", None),
                ('bullet', "Анализ данных и исследования: Python, Pandas, Scikit-learn, AutoML, PatentScope, Elsevier Scopus", None),
            ]),
            ("Образование", [
                ('entry', 'itmo', "Университет ИТМО, 2024 — магистратура по анализу данных", None, [
                    "Диплом: фильтрация с весами Шепли для ML на малых выборках; +7% точности на медицинских данных.",
                ]),
                ('entry', 'hse', "НИУ ВШЭ, 2022 — бакалавриат по программной инженерии", None, [
                    "Диплом: доступный ассистент для слабовидящих пользователей на базе Yandex Cloud OCR.",
                ]),
            ]),
            ("Публикации", [
                ('bullet', "Google Scholar · индекс Хирша 2", "https://scholar.google.com/citations?user=sD1qs3QAAAAJ"),
                ('bullet', "Danilov et al., J. Pers. Med. 2024, 14, 811 — прогнозирование терапии сибутрамином.", "https://doi.org/10.3390/jpm14080811"),
                ('bullet', "Markina et al., J. Clin. Med. 2024, 13, 4151 — бурая жировая ткань и лечение ожирения.", "https://doi.org/10.3390/jcm13144151"),
            ]),
            ("Хакатоны", [
                ('entry', None, "ScienceRAG — исследовательский ассистент-агент на базе GigaChat", None, [
                    ("ScienceRAG: улучшил RAG-поиск по arXiv на GigaChat", "https://youtu.be/ri2OOypFLXc?t=11214", 'yt'),
                ]),
                ('entry', None, "X5 AI Tech Hackathon — алгоритм детекции галлюцинаций", None, [
                    ("X5 AI Tech: детектор галлюцинаций на ruBERT — точность 88%, инференс <0,45 с; топ-10.", "https://codenrock.com/users/79846/certificates/250"),
                ]),
            ]),
            ("Языки", [
                ('bullet', "Русский, английский (B1)", None),
            ]),
        ],
    },
}

def contact_parts(lang):
    loc = I18N[lang]['location']
    return [
        (loc, None, None),
        ('+7 (986) 767-86-96', 'tel:+79867678696', None),
        ('@geniusserg', 'https://t.me/geniusserg', 'tg'),
        ('danilovsergeyd@vk.com', 'mailto:danilovsergeyd@vk.com', 'mail'),
        ('linkedin.com/in/geniusserg', 'https://www.linkedin.com/in/geniusserg/', 'in'),
    ]

def build_page(lang):
    T = I18N[lang]
    parts = []
    parts.append('<div class="langbar">'
                 '<button class="langbtn" data-lang="en" onclick="setLang(\'en\')">EN</button>'
                 '<button class="langbtn" data-lang="ru" onclick="setLang(\'ru\')">RU</button>'
                 '</div>')
    parts.append('<header>')
    parts.append(f'<img class="avatar" src="data:image/png;base64,{photo}" alt="">')
    parts.append('<div class="head">')
    parts.append(f'<h1>{esc(T["name"])}</h1>')
    parts.append('<div class="contact">')
    texts = []
    buttons = []
    for text, url, kind in contact_parts(lang):
        if kind:
            target = ' target="_blank" rel="noopener"' if kind in ('tg', 'in') else ''
            buttons.append(f'<a class="cb cb-{kind}" href="{esc(url)}"{target}>{BTN_SVG[kind]}{esc(text)}</a>')
        else:
            seg = f'<a href="{esc(url)}">{esc(text)}</a>' if url else esc(text)
            texts.append(seg)
    parts.append('<span class="contact-text">' + ' · '.join(texts) + '</span>')
    parts.extend(buttons)
    parts.append('</div></div>')
    pdf_file = 'resume-ru.pdf' if lang == 'ru' else 'resume.pdf'
    pdf_name = 'Danilov_Sergey_Resume_RU.pdf' if lang == 'ru' else 'Danilov_Sergey_Resume.pdf'
    parts.append('<div class="head-right">')
    parts.append(f'<div class="views">👁 <span class="view-count">0</span> {esc(T["views"])}</div>')
    parts.append(f'<a class="btn" href="{pdf_file}" download="{pdf_name}">{esc(T["download"])}</a>')
    parts.append('</div>')
    parts.append('</header>')
    parts.append(f'<div class="summary">{esc(T["summary"])}</div>')
    for heading, items in T['sections']:
        parts.append(f'<h2>{esc(heading)}</h2>')
        for it in items:
            kind = it[0]
            if kind == 'job':
                _, ikey, role, dates, bullets = it
                icon = icon_for(ikey)
                parts.append(f'<div class="job">{icon}<span class="role">{esc(role)}</span> '
                             f'<span class="dates">· {esc(dates)}</span><ul>')
                for b in bullets:
                    if isinstance(b, tuple):
                        btext, bdocs = b
                        parts.append(f'<li>{esc(btext)} <a class="doc-badge" href="{esc(bdocs)}" target="_blank" rel="noopener">{esc(T["doc"])}</a></li>')
                    else:
                        parts.append(f'<li>{esc(b)}</li>')
                parts.append('</ul></div>')
            elif kind == 'entry':
                _, ikey, text, url, subs = it
                icon = icon_for(ikey)
                txt = f'<a href="{esc(url)}">{esc(text)}</a>' if url else esc(text)
                parts.append(f'<div class="entry">{icon}{txt}</div>')
                if subs:
                    parts.append('<ul class="sub">')
                    for s in subs:
                        if isinstance(s, tuple) and len(s) == 3:
                            st, su, badge = s
                        else:
                            st, su = (s if isinstance(s, tuple) else (s, None))
                            badge = None
                        if badge == 'yt':
                            seg = (f'{esc(st)} '
                                   f'<a class="yt" href="{esc(su)}" target="_blank" rel="noopener">{YT_ICON}YouTube</a>')
                        else:
                            seg = f'<a href="{esc(su)}">{esc(st)}</a>' if su else esc(st)
                        parts.append(f'<li>{seg}</li>')
                    parts.append('</ul>')
            elif kind == 'bullet':
                _, text, url = it
                seg = f'<a href="{esc(url)}">{esc(text)}</a>' if url else esc(text)
                if ': ' in text:
                    lab, rest = text.split(': ', 1)
                    seg = f'<span class="stack-label">{esc(lab)}:</span> {esc(rest)}'
                parts.append(f'<ul class="plain"><li>{seg}</li></ul>')
    parts.append('<footer>')
    parts.append(f'<button class="like-btn" onclick="toggleLike()" aria-label="{esc(T["like"])}">'
                 '<svg class="heart" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>'
                 f'<span class="like-label" data-like="{esc(T["like"])}" data-liked="{esc(T["liked"])}">{esc(T["like"])}</span>'
                 '<span class="like-count">0</span>'
                 '</button>')
    parts.append('<div class="foot-contact">' + ''.join(buttons) + '</div>')
    parts.append(f'<div class="foot-note">{esc(T["footer"])}</div>')
    parts.append('</footer>')
    return '\n'.join(parts)

CSS = '''
<style>
  :root { --accent:#1a56db; --ink:#111827; --muted:#6b7280; --line:#e5e7eb; }
  * { box-sizing: border-box; }
  body { margin:0; background:#f3f4f6; color:var(--ink);
         font:15px/1.55 "Helvetica Neue", Helvetica, Arial, "Segoe UI", Roboto, sans-serif; }
  a { color:var(--accent); text-decoration:none; }
  a:hover { text-decoration:underline; }
  .langbar { position:absolute; top:14px; right:14px; display:flex; gap:3px; background:#fff;
             border:1px solid var(--line); border-radius:999px; padding:3px; box-shadow:0 1px 4px rgba(0,0,0,.08); }
  .langbtn { border:0; background:transparent; color:var(--muted); font-weight:600; font-size:12px;
             padding:5px 12px; border-radius:999px; cursor:pointer; letter-spacing:.3px; }
  .langbtn.active { background:var(--accent); color:#fff; }
  .page { position:relative; max-width:820px; margin:24px auto; background:#fff; border:1px solid var(--line);
          border-radius:10px; box-shadow:0 1px 3px rgba(0,0,0,.06); padding:40px 44px; }
  header { display:flex; align-items:center; gap:22px; border-bottom:2px solid var(--ink); padding-bottom:18px; }
  .avatar { width:92px; height:92px; border-radius:50%; object-fit:cover; flex:0 0 auto; border:2px solid var(--line); }
  .head h1 { margin:0; font-size:30px; letter-spacing:.2px; }
  .head .contact { margin-top:10px; color:var(--muted); font-size:13.5px;
                   display:flex; flex-wrap:wrap; align-items:center; gap:10px; }
  .head .contact .contact-text a { color:var(--accent); }
  .views { color:var(--muted); font-size:12.5px; white-space:nowrap; }
  .head-right { margin-left:auto; display:flex; flex-direction:column; align-items:flex-end; gap:6px; flex:0 0 auto; }
  .btn { background:var(--accent); color:#fff; padding:10px 16px; border-radius:8px;
         font-weight:600; font-size:14px; white-space:nowrap; }
  .btn:hover { text-decoration:none; filter:brightness(1.08); }
  .cb { display:inline-flex; align-items:center; gap:6px; padding:4px 14px; border-radius:999px;
        color:var(--cb-color); font-weight:400; font-size:13px; vertical-align:middle;
        background:transparent; border:1.5px solid var(--cb-color);
        transition: transform .18s ease, background .18s ease, box-shadow .18s ease; }
  .cb svg { width:14px; height:14px; fill:currentColor; transition: transform .18s ease; }
  .cb:hover { transform: translateY(-2px); background:var(--cb-tint); text-decoration:none; }
  .cb:hover svg { transform: translate(2px, -2px); }
  .cb:active { transform: translateY(0) scale(.96); }
  .cb-tg { --cb-color:#2d9be0; --cb-tint:rgba(45,155,224,.10); }
  .cb-mail { --cb-color:#e63946; --cb-tint:rgba(230,57,70,.10); }
  .cb-in { --cb-color:#0a66c2; --cb-tint:rgba(10,102,194,.10); }
  .yt { display:inline-flex; align-items:center; gap:5px; background:#FF0000; color:#fff;
        padding:2px 10px; border-radius:999px; font-weight:500; font-size:12px; vertical-align:middle;
        transition: transform .15s ease, box-shadow .15s ease; }
  .yt:hover { transform: translateY(-1px); box-shadow: 0 4px 12px rgba(255,0,0,.4); text-decoration:none; }
  .summary { margin:20px 0 4px; font-size:16px; line-height:1.6; color:#1f2937;
             border-left:4px solid var(--accent); padding:6px 0 6px 16px; }
  h2 { text-transform:uppercase; font-size:13px; letter-spacing:1.4px; color:var(--accent);
       border-bottom:1px solid var(--line); padding-bottom:5px; margin:26px 0 12px; }
  .job { margin:0 0 14px; }
  .job .role { font-weight:700; }
  .job .dates { color:var(--muted); font-style:italic; white-space:nowrap; }
  .cicon { width:16px; height:16px; border-radius:3px; margin-right:7px; vertical-align:-3px; object-fit:contain; }
  .doc-badge { display:inline-flex; align-items:center; gap:4px; font-size:11.5px; font-weight:600;
               color:var(--accent); border:1px solid var(--accent); border-radius:999px; padding:1px 9px;
               vertical-align:1px; white-space:nowrap; text-decoration:none; }
  .doc-badge:hover { background:var(--accent); color:#fff; text-decoration:none; }
  ul { margin:4px 0 0; padding-left:20px; }
  li { margin:2px 0; }
  .sub { list-style:none; padding-left:18px; color:#374151; }
  .sub li::before { content:"–  "; color:var(--muted); }
  .entry { font-weight:600; margin:10px 0 2px; }
  .plain { list-style:none; padding-left:0; }
  .plain li { padding-left:18px; text-indent:-18px; }
  .plain li::before { content:"•  "; color:var(--accent); }
  .stack-label { font-weight:600; }
  footer { margin-top:26px; text-align:center; color:var(--muted); font-size:12px; }
  .like-btn { display:inline-flex; align-items:center; gap:7px; background:#fff; border:1.5px solid var(--line);
              color:var(--muted); padding:7px 18px; border-radius:999px; cursor:pointer; font-size:14px; font-weight:500;
              transition: transform .15s ease, border-color .2s ease, color .2s ease, background .2s ease; }
  .like-btn:disabled { opacity:.5; cursor:not-allowed; }
  .like-btn .heart { width:16px; height:16px; fill:transparent; stroke:currentColor; stroke-width:2;
                     transition: fill .2s ease; }
  .like-btn:hover { border-color:#f43f5e; color:#f43f5e; }
  .like-btn.liked { border-color:#f43f5e; color:#f43f5e; background:#fff1f2; }
  .like-btn.liked .heart { fill:#f43f5e; stroke:#f43f5e; }
  .like-btn.pop .heart { animation: heartPop .4s ease; }
  .like-count { background:var(--line); color:var(--muted); border-radius:999px; padding:0 8px;
                font-size:12px; line-height:18px; min-width:18px; text-align:center; }
  .like-btn.liked .like-count { background:#ffe4e6; color:#f43f5e; }
  @keyframes heartPop { 0%{transform:scale(1)} 35%{transform:scale(1.45)} 70%{transform:scale(.9)} 100%{transform:scale(1)} }
  .foot-note { margin-top:10px; }
  .foot-contact { display:flex; flex-wrap:wrap; justify-content:center; align-items:center; gap:10px; margin-top:14px; }
  @media (max-width:560px){ .page{padding:24px 18px;margin:0;border:0;border-radius:0} header{flex-direction:column;text-align:center} .head-right{margin-left:0;align-items:center} h1{font-size:26px} }
  @keyframes fadeUp { from { opacity:0; transform: translateY(14px); } to { opacity:1; transform: translateY(0); } }
  .page { animation: fadeUp .55s cubic-bezier(.2,.7,.3,1) both; }
  @media (prefers-reduced-motion: reduce){ .page,.cb,.cb svg,.btn{ animation:none; transition:none; } }
  @page { size:A4; margin:12mm 14mm; }
  @media print{
    body{ background:#fff; }
    .page{ border:0; box-shadow:none; margin:0; max-width:none; border-radius:0; padding:0; animation:none; }
    .btn,.langbar,.like-btn,.views,.foot-contact{ display:none; }
    .cb{ box-shadow:none; }
  }
</style>'''

JS = '''
<script>
function setLang(l) {
  document.getElementById('page-en').hidden = (l !== 'en');
  document.getElementById('page-ru').hidden = (l !== 'ru');
  document.querySelectorAll('.langbtn').forEach(function(b){
    b.classList.toggle('active', b.dataset.lang === l);
  });
  document.documentElement.lang = l;
  document.title = (l === 'ru') ? 'Данилов Сергей Дмитриевич — Резюме' : 'Danilov Sergey Dmitrievich — Resume';
  try { localStorage.setItem('lang', l); } catch(e) {}
}
var saved = null;
try { saved = localStorage.getItem('lang'); } catch(e) {}
var qs = (location.search || '').match(/lang=(en|ru)/);
var initial = (qs && qs[1]) || saved || ((navigator.language || '').slice(0,2) === 'ru' ? 'ru' : 'en');
setLang(initial);

var UPSTASH_URL = 'https://romantic-pug-216854.upstash.io';
var UPSTASH_TOKEN = 'gQAAAAAAA08WAAIgcDIwYjE5ZTQwOThmM2U0NTdlYWYyMzg2NzM5MzVlMDFiMw';
var LIKE_KEY = 'like_count';
var MAX_TOGGLES = 10;
var VIEW_KEY = 'view_count';

function upstash(cmd) {
  return fetch(UPSTASH_URL, {
    method: 'POST',
    headers: { 'Authorization': 'Bearer ' + UPSTASH_TOKEN, 'Content-Type': 'application/json' },
    body: JSON.stringify(cmd)
  }).then(function(r){ return r.json(); });
}

function applyLike(liked) {
  document.querySelectorAll('.like-btn').forEach(function(b){
    b.classList.toggle('liked', liked);
    var lbl = b.querySelector('.like-label');
    if (lbl) lbl.textContent = liked ? (lbl.dataset.liked || 'Liked') : (lbl.dataset.like || 'Like');
  });
}

function setCount(n) {
  document.querySelectorAll('.like-count').forEach(function(el){ el.textContent = n; });
}

function setViewCount(n) {
  document.querySelectorAll('.view-count').forEach(function(el){ el.textContent = n; });
}

function getToggles() {
  var n = 0;
  try { n = parseInt(localStorage.getItem('resume-toggle-count'), 10); } catch(e) {}
  return isNaN(n) ? 0 : n;
}

function updateLimitUI(toggles) {
  var locked = toggles >= MAX_TOGGLES;
  document.querySelectorAll('.like-btn').forEach(function(b){
    b.disabled = locked;
    b.classList.toggle('locked', locked);
  });
}

function toggleLike() {
  var toggles = getToggles();
  if (toggles >= MAX_TOGGLES) return;

  var liked = null;
  try { liked = localStorage.getItem('resume-liked') === '1'; } catch(e) { liked = false; }
  var newLiked = !liked;
  var cmd = newLiked ? 'INCR' : 'DECR';

  document.querySelectorAll('.like-btn').forEach(function(b){ b.disabled = true; });

  upstash([cmd, LIKE_KEY]).then(function(d){
    var n = parseInt(d && d.result, 10);
    if (!isNaN(n)) setCount(n < 0 ? 0 : n);
    try { localStorage.setItem('resume-liked', newLiked ? '1' : '0'); } catch(e) {}
    toggles += 1;
    try { localStorage.setItem('resume-toggle-count', String(toggles)); } catch(e) {}
    applyLike(newLiked);
    document.querySelectorAll('.like-btn').forEach(function(b){
      b.classList.remove('pop'); void b.offsetWidth; b.classList.add('pop');
    });
    updateLimitUI(toggles);
  }).catch(function(){
    updateLimitUI(toggles);
  });
}

(function(){
  var liked = null;
  try { liked = localStorage.getItem('resume-liked') === '1'; } catch(e) { liked = false; }
  applyLike(liked);
  updateLimitUI(getToggles());
  upstash(['GET', LIKE_KEY]).then(function(d){
    var n = parseInt(d && d.result, 10);
    if (!isNaN(n)) setCount(n < 0 ? 0 : n);
  }).catch(function(){});
  var viewed = null;
  try { viewed = localStorage.getItem('resume-viewed') === '1'; } catch(e) { viewed = false; }
  if (viewed) {
    upstash(['GET', VIEW_KEY]).then(function(d){
      var n = parseInt(d && d.result, 10);
      if (!isNaN(n)) setViewCount(n);
    }).catch(function(){});
  } else {
    upstash(['INCR', VIEW_KEY]).then(function(d){
      var n = parseInt(d && d.result, 10);
      if (!isNaN(n)) setViewCount(n);
      try { localStorage.setItem('resume-viewed', '1'); } catch(e) {}
    }).catch(function(){});
  }
})();
</script>'''

SEO_HEAD = '''
<meta name="description" content="Danilov Sergey Dmitrievich — LLM Inference R&D Engineer (Huawei). Distributed LLM inference, GPU orchestration, MoE, vLLM, PyTorch, C++, Kubernetes. Saint Petersburg, Russia.">
<meta name="keywords" content="LLM inference engineer, ML engineer, AI engineer, distributed systems, GPU orchestration, vLLM, MoE, PyTorch, C++, Kubernetes, XGBoost, RAG, Sergey Danilov, Danilov Sergey, resume, CV, Saint Petersburg">
<meta name="author" content="Danilov Sergey Dmitrievich">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://geniusserg.github.io/">
<meta property="og:type" content="profile">
<meta property="og:title" content="Danilov Sergey Dmitrievich — LLM Inference R&D Engineer">
<meta property="og:description" content="LLM inference, distributed systems, GPU orchestration, MoE, vLLM. Resume / CV.">
<meta property="og:url" content="https://geniusserg.github.io/">
<meta property="og:image" content="https://geniusserg.github.io/photo.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Danilov Sergey Dmitrievich — LLM Inference R&D Engineer">
<meta name="twitter:description" content="LLM inference, distributed systems, GPU orchestration, MoE, vLLM.">
<meta name="twitter:image" content="https://geniusserg.github.io/photo.png">
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Danilov Sergey Dmitrievich",
  "alternateName": ["Sergey Danilov", "geniusserg"],
  "url": "https://geniusserg.github.io/",
  "image": "https://geniusserg.github.io/photo.png",
  "jobTitle": "LLM Inference R&D Engineer",
  "worksFor": {"@type": "Organization", "name": "Huawei"},
  "alumniOf": [
    {"@type": "CollegeOrUniversity", "name": "ITMO University"},
    {"@type": "CollegeOrUniversity", "name": "Higher School of Economics"}
  ],
  "address": {"@type": "PostalAddress", "addressLocality": "Saint Petersburg", "addressCountry": "RU"},
  "sameAs": [
    "https://www.linkedin.com/in/geniusserg/",
    "https://t.me/geniusserg",
    "https://github.com/geniusserg",
    "https://scholar.google.com/citations?user=sD1qs3QAAAAJ"
  ],
  "knowsAbout": ["LLM inference", "distributed systems", "GPU orchestration", "vLLM", "MoE", "PyTorch", "C++", "Kubernetes", "XGBoost", "RAG", "recommender systems"]
}
</script>
'''

html_out = ['<!doctype html>',
            '<html lang="en"><head><meta charset="utf-8">',
            '<meta name="viewport" content="width=device-width, initial-scale=1">',
            '<title>Danilov Sergey Dmitrievich — Resume</title>',
            SEO_HEAD,
            CSS,
            '</head><body>',
            f'<div class="page" id="page-en" lang="en">{build_page("en")}</div>',
            f'<div class="page" id="page-ru" lang="ru" hidden>{build_page("ru")}</div>',
            JS,
            '</body></html>']

if __name__ == '__main__':
    out = '\n'.join(html_out)
    open('/tmp/cv_deploy/index.html', 'w').write(out)
    print("wrote index.html", len(out), "bytes")
