#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сборка «цифрового сада» — статический сайт без зависимостей.
Запуск: python3 _build/build.py
"""
import os, html, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://nsbshal-arch.github.io/sad"
TITLE = "Вестник адекватности"
AUTHOR = "Надежда Добрынина"
TAGLINE = "цифровой сад"
UPDATED = "2026-11-24"

STATUS = {
    "seed": ("росток", "Заметка только проклюнулась: мысль есть, выводов пока нет."),
    "draft": ("черновик", "Собрано, но не отшлифовано. Может поменяться."),
    "ever": ("зрелая", "Устоявшаяся заметка. Ссылаться можно."),
}

# ---------------------------------------------------------------- content ---
NOTES = [
    {
        "slug": "zabota-zakanchivaetsya",
        "title": "Забота заканчивается там, где начинается «ты же тут работала»",
        "status": "ever",
        "date": "2026-11-21",
        "tags": ["забота", "адаптация", "декрет", "HR-бренд"],
        "excerpt": "Компании вкладываются во вход: вау-кухни, пять этапов собеседований, мерч. "
                   "А человек, который возвращается после декрета, приходит в ту же компанию — "
                   "и его встречают как незнакомца. Приём — это не финиш, а вход в здание.",
        "related": ["obuchenie-zaplatili", "ritm-ne-sporit"],
        "body": """
<p class="lead">За кандидата с рынка идёт настоящая война: конкурсы на вакансии, приветственные наборы, пять этапов собеседований. За <b>вход</b> платят — потому что его видно в отчёте.</p>

<p>А потом человек выходит на работу. И если он уже здесь работал, его встречают по принципу «ты же тут была, сама разберёшься». Это слепое пятно: забота заканчивается ровно там, где начинается эта фраза.</p>

<h2>Пример, который поднимает бренд сильнее рекламы</h2>

<p>Девушка возвращается после декрета. Она могла быть в штате — а могла прийти «с улицы», впервые, уже с ребёнком. В обоих случаях проблема одна: она не знает, как здесь всё устроено, и боится выглядеть глупо.</p>

<p>Мы помогли ей освоиться. Не потому что обязаны — а потому что иначе человек выходит в пустоту и уходит через два месяца. Заботу легко написать на сайте. Трудно — встретить человека, который полтора года не был в офисе, и сделать так, чтобы он вышел спокойным.</p>

<h2>Почему это про клиента, а не «про доброту»</h2>

<p>Работодатель — не институт социальных гарантий, и делать вид, что забота о сотруднике — его прямая обязанность, бессмысленно. Он считает деньги. Но есть связка, которая делает заботу выгодной:</p>

<blockquote>Выгоревший и обиженный сотрудник плохо обслуживает клиента.</blockquote>

<p>Человек, который вышел на работу в тревоге, либо уходит через два месяца, либо остаётся — и работает «на автомате». И то и другое видит клиент: в тоне, в качестве, в фразах «я тут новенькая, не знаю». Забота о сотрудниках — это защита клиентского опыта, а не благотворительность.</p>

<h2>Что нужно сделать на самом деле</h2>

<p>Почти ничего. Не нужен бюджет и полугодовой проект — нужны две вещи: назвать ситуацию своим именем и добавить рамки в уже существующий процесс.</p>

<ul>
  <li><b>Статус при оформлении.</b> «Из декрета» — отдельный сценарий адаптации, как «первое место работы». Сейчас почти нигде не различают, и всех ведут одной дорогой.</li>
  <li><b>Первое сообщение до выхода.</b> Не «когда выходите», а «мы тебя ждали».</li>
  <li><b>Первый день без подвигов.</b> Проговорить прямо: возвращаться «как будто не уходила» не требуется.</li>
  <li><b>Наставник, который отвечает за результат,</b> а не просто «числится».</li>
</ul>

<p>Ноль дополнительных затрат. Но есть ответственность, которую компания на себя берёт: довести человека до нормы, а не сделать вид, что он сам справится.</p>

<h2>Что пока не решено</h2>

<p>Я не знаю, как честно посчитать эффект, не притворяясь, что все цифры известны. Ставки и число возвращений — факт, а стоимость закрытия вакансии и доходимость — допущения. Пока держу их явно помеченными, а не выдаю за измерение.</p>
""",
    },
    {
        "slug": "obuchenie-zaplatili",
        "title": "Обучение, за которое заплатили и не получили",
        "status": "draft",
        "date": "2026-11-19",
        "tags": ["обучение", "L&D", "эффективность", "сервис"],
        "excerpt": "Бюджеты на обучение выделяются — вопрос не в том, купят ли. Вопрос в том, что компания "
                   "получает на выходе. Обычно — галочку в отчёте: «обучение проведено, охват 100%».",
        "related": ["zabota-zakanchivaetsya", "adekvatnost-kak-professiya"],
        "body": """
<p class="lead">Сразу разделю два разных разговора, которые постоянно смешивают.</p>

<p><b>Развитие по желанию сотрудника</b> — это его деньги, его мотивация и его ответственность. К компании это не относится, и делать вид, что она должна «развить» взрослого человека, странно: он может уйти в любой момент, и вложение уйдёт с ним.</p>

<p><b>Обязательное обучение</b> — другое. Это то, что компания считает необходимым для работы: внешний курс, внутренний тест, «сдай регламент», «ознакомься с обновлением». Оба вида — про одно: поддержание уровня сервиса и качества. Не про амбиции, не про карьеру.</p>

<h2>Проблема</h2>

<p>Компания покупает обучение. Договоры заключаются, программы запускаются. Вопрос не «купят ли» — купят. Вопрос в том, что получается на выходе.</p>

<p>На выходе — галочка в отчёте. А поведение не изменилось: люди работают так же, как работали. Боль заказчика звучит так: «я потратил бюджет и не могу показать, что уровень сервиса вырос».</p>

<h2>Почему не работает</h2>

<p>Обучение живёт отдельно от работы. Оно не встроено в процесс, не привязано к задаче и ни к чему не обязывает. Сотрудник приходит «после смены» или «в свой выходной», слушает сорок минут и возвращается к конвейеру — где всё по-прежнему.</p>

<p>Два сдвига, которые это меняют:</p>

<ul>
  <li><b>Время.</b> Всё обучение — в рабочее время. Не как льгота, а как норма: если выделено два часа, они должны быть потрачены осмысленно.</li>
  <li><b>Мера.</b> Меряют прохождение, а не навык. «Охват 100%» ничего не говорит о качестве. Говорит — показатель после обучения: меньше ошибок, короче путь до самостоятельного решения, выше оценка звонков.</li>
</ul>

<h2>Формат, который работал</h2>

<p>Видео на двадцать минут, домашнее задание ещё на двадцать, встреча раз в неделю на два часа. Всё — в рабочее время. Компании были разного уровня: онлайн-школы со средним чеком двадцать тысяч и с чеком пятьсот тысяч. Обучение шло онлайн — и это работало.</p>

<p>Если компания может оторвать человека от работы, чтобы его обучал живой человек, — это дорого. Именно поэтому наставник показывает серьёзность намерения: компания покупает не контент, а время людей.</p>

<h2>Где сложно</h2>

<p>В жёстком сменном графике — контакт-центр, звонок за звонком — установить это напрямую тяжело. Но и там работает: не планировать обучение и релизы на пиковые дни, не размазывать модуль на месяц, не лить воду. Принцип не меняется, меняется механика.</p>

<h2>Что пока не решено</h2>

<p>Гейт на практике. Что происходит, если человек не прошёл обязательное обучение? Пока это не продумано, принцип держится на доброй воле руководителя — а значит, держится плохо.</p>
""",
    },
    {
        "slug": "adekvatnost-kak-professiya",
        "title": "Адекватность — это профессия",
        "status": "seed",
        "date": "2026-11-16",
        "tags": ["мышление", "работа", "наблюдение"],
        "excerpt": "Не «быть хорошим», а не врать себе о данных. Называть вещи своими именами, "
                   "когда это неудобно, и не путать желаемое с измеренным.",
        "related": ["obuchenie-zaplatili", "cennosti-na-plakatah"],
        "body": """
<p class="lead">Короткая заметка, которая пока только проклюнулась.</p>

<p>Адекватность в работе — это не мягкость и не «позитивный настрой». Это способность не врать себе о том, что показывают данные, и называть вещи своими именами, даже когда название неудобное.</p>

<p>Три вещи, которые я за этим вижу:</p>

<ul>
  <li><b>Не путать желаемое с измеренным.</b> «Стало лучше» — не аргумент. Аргумент — что именно и насколько.</li>
  <li><b>Не прятать неприятное в формулировках.</b> «Зона роста» вместо «не справляется» экономит минуту и стоит месяца.</li>
  <li><b>Отличать своё мнение от факта.</b> Особенно когда мнение сильное.</li>
</ul>

<p>Мне это нужно не для красоты. Без этого нельзя ни учить, ни строить процессы: любая система, построенная на приукрашенных данных, разваливается на первом же реальном потоке.</p>

<p><i>Дальше: хочу разобрать, как это выглядит в разговоре с руководителем, который уверен, что «проблема в людях».</i></p>
""",
    },
    {
        "slug": "ritm-ne-sporit",
        "title": "Ритм: не спорить с телом",
        "status": "draft",
        "date": "2026-11-22",
        "tags": ["ритм", "продукт", "ресурс", "выгорание"],
        "excerpt": "Приложение, которое не заставляет быть продуктивной, а помогает планировать "
                   "сложное на дни силы. Сейчас — прототип, который можно поставить на телефон.",
        "related": ["zabota-zakanchivaetsya", "adekvatnost-kak-professiya"],
        "body": """
<p class="lead">Все трекеры, которые я видела, устроены одинаково: они оценивают. Серия дней, проценты, красные шкалы, «вы отстаёте от плана». Я хотела сделать противоположное.</p>

<h2>Идея</h2>

<p>Энергия не ровная. Есть дни, когда сложный разговор даётся легко, и дни, когда два письма — уже подвиг. Если планировать, не глядя на это, календарь начинает врать: важное падает на дни спада, и человек либо перегружается, либо решает, что «со мной что-то не так».</p>

<p>«Ритм» не лечит и не воспитывает. Он делает три вещи: даёт назвать свои фазы своими словами, за пять секунд отметить уровень энергии и подсказывает, что перенести, а что оставить.</p>

<h2>Чего в нём нет</h2>

<ul>
  <li>Нет серий и штрафов за пропуски.</li>
  <li>Нет оценок «хорошо/плохо».</li>
  <li>Нет медицинских терминов и диагнозов.</li>
  <li>Нет красных шкал выгорания.</li>
</ul>

<p>Это не мелочи. Именно они превращают заботу в ещё один источник стресса.</p>

<h2>Где я сейчас</h2>

<p>Есть работающий прототип: экран «Сегодня» с картой дня, свои названия фаз, отметка энергии, «бережное предложение» и мягкий план. Календарь и бытовая забота — в проработке.</p>

<p>Сейчас он живёт как приложение, которое ставится на телефон и работает офлайн — чтобы можно было дать людям и посмотреть, пользуются ли они им на третий день, а не на первый.</p>

<h2>Что пока не решено</h2>

<p>Главный вопрос — не технический. Будут ли люди отмечать энергию, если это необязательно? Или это ещё одна красивая вещь, которую открывают дважды? На этот вопрос ответит только тест, поэтому я и не спешу с выводами.</p>
""",
    },
    {
        "slug": "cennosti-na-plakatah",
        "title": "Ценности на плакатах не работают",
        "status": "draft",
        "date": "2026-11-14",
        "tags": ["культура", "ценности", "руководители"],
        "excerpt": "Ценности видны не в декларации, а в неудобный момент: когда нужно выбрать между "
                   "человеком и планом. Всё, что написано на стене, проверяется там.",
        "related": ["adekvatnost-kak-professiya", "zabota-zakanchivaetsya"],
        "body": """
<p class="lead">Любая компания может написать на стене, что люди — главная ценность. Это ничего не стоит и ни к чему не обязывает.</p>

<p>Ценности проверяются в неудобный момент. Когда сильный сотрудник провалил проект и надо решить: разбираться или искать виноватого. Когда человек просит перенести встречу из-за ребёнка. Когда руководитель врёт в отчёте, а он удобный.</p>

<p>В такие моменты и становится видно, что за декларация: рамка для решений или текст на стене.</p>

<h2>Почему плакаты не работают</h2>

<ul>
  <li><b>Они описывают желаемое, а не происходящее.</b> Люди читают не слова, а поведение вокруг.</li>
  <li><b>Их нельзя проверить.</b> «Мы открыты» — не проверяется. «Плохие новости сообщаем первыми» — проверяется.</li>
  <li><b>Они не помогают выбирать.</b> Ценность нужна в момент выбора между двумя хорошими вариантами, а не в презентации.</li>
</ul>

<h2>Что работает вместо</h2>

<p>Правила, по которым можно принять решение без советника. Не «мы за развитие», а «на обучение в рабочее время руководитель выделяет часы и не отзывает с него людей». Не «мы за заботу», а «вернувшегося после декрета встречает наставник, и он отвечает за результат».</p>

<p>Чем конкретнее правило, тем сильнее оно выглядит как ценность — и тем труднее его имитировать.</p>
""",
    },
]

SECTIONS = [
    ("Сад", "index.html"),
    ("Заметки", "notes.html"),
    ("Сейчас", "now.html"),
    ("Обо мне", "about.html"),
]

# ------------------------------------------------------------------ shell ---
def shell(prefix, page_title, body, description="", page_url=""):
    nav = "".join(
        f'<a href="{prefix}{href}">{name}</a>' for name, href in SECTIONS
    )
    full_title = f"{page_title} — {TITLE}" if page_title else f"{TITLE} — {TAGLINE}"
    desc = html.escape(description or "Цифровой сад Надежды Добрыниной: заметки о работе с людьми, обучении и заботе без пафоса.")
    url = f"{SITE}/{page_url}" if page_url else f"{SITE}/"
    return f"""<!DOCTYPE html>
<html lang="ru" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(full_title)}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="{TITLE}">
<meta name="twitter:card" content="summary">
<link rel="alternate" type="application/rss+xml" title="{TITLE}" href="{prefix}rss.xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Oswald:wght@400;500;600&family=Playfair+Display:ital,wght@0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}style.css">
<script>
  (function () {{
    var t = null;
    try {{ t = localStorage.getItem("sad-theme"); }} catch (e) {{}}
    if (!t && window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) t = "dark";
    if (t) document.documentElement.setAttribute("data-theme", t);
  }})();
</script>
</head>
<body>
<div class="progress" id="progress" aria-hidden="true"></div>
<header class="site-head">
  <div class="wrap head-inner">
    <a class="wordmark" href="{prefix}index.html">
      <span class="wm-main">Вестник<br>адекватности</span>
      <span class="wm-sub">{TAGLINE}</span>
    </a>
    <nav class="site-nav">{nav}</nav>
    <button class="theme-toggle" id="themeToggle" aria-label="Сменить тему" title="Сменить тему">
      <span class="tt-sun">☀</span><span class="tt-moon">☾</span>
    </button>
  </div>
</header>
{body}
<footer class="site-foot">
  <div class="wrap foot-inner">
    <div class="foot-col">
      <div class="foot-brand">Вестник адекватности</div>
      <p class="foot-note">Сад растёт: заметки не финальные. То, что сегодня черновик, завтра может стать другим.</p>
    </div>
    <div class="foot-col">
      <div class="foot-label">Разделы</div>
      <ul class="foot-list">{''.join(f'<li><a href="{prefix}{href}">{name}</a></li>' for name, href in SECTIONS)}<li><a href="{prefix}rss.xml">RSS</a></li></ul>
    </div>
    <div class="foot-col">
      <div class="foot-label">Связь</div>
      <ul class="foot-list">
        <li><a href="mailto:nsbshal@gmail.com">nsbshal@gmail.com</a></li>
        <li><a href="https://t.me/vestnik_adekvatnosti" target="_blank" rel="noopener">Telegram ↗</a></li>
      </ul>
    </div>
    <div class="foot-col foot-col-wide">
      <div class="foot-label">Колофон</div>
      <p class="foot-note">© 2026 {AUTHOR}. Набрано Playfair Display, Oswald и Inter. Собрано вручную, без конструкторов. <span class="foot-upd">Обновлено {UPDATED}.</span></p>
    </div>
  </div>
</footer>
<script src="{prefix}script.js" defer></script>
</body>
</html>
"""


def status_chip(key):
    name, hint = STATUS[key]
    return f'<span class="chip chip-{key}" title="{html.escape(hint)}">{name}</span>'


# ------------------------------------------------------------------ pages ---
def build_index():
    cards = []
    for n in NOTES:
        tags = "".join(f'<span class="tag">{html.escape(t)}</span>' for t in n["tags"][:3])
        cards.append(f"""
        <a class="note-card" href="notes/{n['slug']}.html">
          <div class="nc-top">{status_chip(n['status'])}<span class="nc-date">{n['date']}</span></div>
          <h3 class="nc-title">{html.escape(n['title'])}</h3>
          <p class="nc-excerpt">{html.escape(n['excerpt'])}</p>
          <div class="nc-tags">{tags}</div>
        </a>""")

    body = f"""
<main>
  <section class="hero">
    <div class="wrap">
      <div class="kicker">цифровой сад · {AUTHOR}</div>
      <h1 class="hero-title">Мысли, которые<br>я&nbsp;не&nbsp;хочу терять</h1>
      <p class="hero-lead">Здесь лежат заметки о работе с людьми: адаптация, обучение, культура, забота. Не статьи «для публикации», а то, что я думаю, проверяю и переписываю. Сад, а не журнал: заметки растут.</p>
      <div class="hero-meta">
        <span>{len(NOTES)} заметок</span>
        <span class="dot">·</span>
        <span>обновлено {UPDATED}</span>
        <span class="dot">·</span>
        <a href="rss.xml">RSS</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="sec-head">
        <h2 class="sec-title">Что здесь растёт</h2>
        <div class="legend">
          <span class="chip chip-seed">росток</span>
          <span class="chip chip-draft">черновик</span>
          <span class="chip chip-ever">зрелая</span>
        </div>
      </div>
      <div class="notes-grid">{''.join(cards)}
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="wrap">
      <div class="about-strip">
        <div class="as-text">
          <div class="kicker">кто это пишет</div>
          <h2 class="sec-title">Надежда Добрынина</h2>
          <p>Двадцать лет в обучении, внутренних коммуникациях и управленческом консалтинге. Настраиваю HR-процессы так, чтобы они работали, а не выглядели. Пишу про то, что вижу вблизи.</p>
          <p><a class="link-arrow" href="about.html">Подробнее обо мне →</a></p>
        </div>
        <div class="as-links">
          <a class="quick" href="now.html"><span class="q-label">Сейчас</span><span class="q-text">чем занята в этом месяце</span></a>
          <a class="quick" href="notes.html"><span class="q-label">Все заметки</span><span class="q-text">список и теги</span></a>
          <a class="quick" href="https://nsbshal-arch.github.io/portfolio-v2/" target="_blank" rel="noopener"><span class="q-label">Портфолио ↗</span><span class="q-text">кейсы с цифрами</span></a>
        </div>
      </div>
    </div>
  </section>
</main>"""
    return shell("", "", body, page_url="")


def build_notes_list():
    rows = []
    for n in sorted(NOTES, key=lambda x: x["date"], reverse=True):
        rows.append(f"""
        <a class="note-row" href="notes/{n['slug']}.html">
          <span class="nr-date">{n['date']}</span>
          <span class="nr-body">
            <span class="nr-title">{html.escape(n['title'])}</span>
            <span class="nr-excerpt">{html.escape(n['excerpt'])}</span>
          </span>
          <span class="nr-status">{status_chip(n['status'])}</span>
        </a>""")

    alltags = {}
    for n in NOTES:
        for t in n["tags"]:
            alltags[t] = alltags.get(t, 0) + 1
    tags_html = "".join(f'<span class="tag">{html.escape(t)}<i>{c}</i></span>' for t, c in sorted(alltags.items()))

    body = f"""
<main>
  <section class="page-head">
    <div class="wrap">
      <div class="kicker">все заметки</div>
      <h1 class="page-title">Заметки</h1>
      <p class="page-lead">Порядок — по дате последнего изменения. Статус говорит, насколько заметке можно верить.</p>
      <div class="tag-cloud">{tags_html}</div>
    </div>
  </section>
  <section class="section section-tight">
    <div class="wrap">
      <div class="notes-list">{''.join(rows)}
      </div>
    </div>
  </section>
</main>"""
    return shell("", "Заметки", body, page_url="notes.html")


def build_note(n):
    idx = NOTES.index(n)
    prev_n = NOTES[idx - 1] if idx > 0 else None
    next_n = NOTES[idx + 1] if idx < len(NOTES) - 1 else None
    nav = []
    if prev_n:
        nav.append(f'<a class="pn prev" href="{prev_n["slug"]}.html"><span>← предыдущая</span><b>{html.escape(prev_n["title"])}</b></a>')
    if next_n:
        nav.append(f'<a class="pn next" href="{next_n["slug"]}.html"><span>следующая →</span><b>{html.escape(next_n["title"])}</b></a>')

    rel = [x for x in NOTES if x["slug"] in n["related"]]
    rel_html = ""
    if rel:
        items = "".join(
            f'<a class="rel" href="{r["slug"]}.html"><span class="rel-st">{STATUS[r["status"]][0]}</span><span class="rel-t">{html.escape(r["title"])}</span></a>'
            for r in rel
        )
        rel_html = f"""
      <aside class="related">
        <div class="foot-label">Связанные заметки</div>
        {items}
      </aside>"""

    tags = "".join(f'<span class="tag">{html.escape(t)}</span>' for t in n["tags"])

    body = f"""
<main>
  <article class="note">
    <div class="wrap note-wrap">
      <div class="note-head">
        <a class="back" href="../notes.html">← все заметки</a>
        <div class="note-meta">{status_chip(n['status'])}<span class="nm-date">{n['date']}</span></div>
        <h1 class="note-title">{html.escape(n['title'])}</h1>
        <div class="note-tags">{tags}</div>
        <p class="status-hint">{html.escape(STATUS[n['status']][1])}</p>
      </div>
      <div class="prose">
{n['body']}
      </div>
      {rel_html}
      <nav class="pn-nav">{''.join(nav)}</nav>
      <div class="note-foot">
        <p>Заметка растёт: если что-то поменялось — она поменяется тоже. Написать: <a href="mailto:nsbshal@gmail.com">nsbshal@gmail.com</a> или <a href="https://t.me/vestnik_adekvatnosti" target="_blank" rel="noopener">в Telegram</a>.</p>
      </div>
    </div>
  </article>
</main>"""
    return shell("../", n["title"], body, description=n["excerpt"], page_url=f"notes/{n['slug']}.html")


def build_about():
    body = f"""
<main>
  <section class="page-head">
    <div class="wrap">
      <div class="kicker">обо мне</div>
      <h1 class="page-title">Надежда Добрынина</h1>
      <p class="page-lead">Настраиваю HR-процессы так, чтобы они работали, а не выглядели. Двадцать лет в обучении, внутренних коммуникациях и управленческом консалтинге.</p>
    </div>
  </section>
  <section class="section section-tight">
    <div class="wrap about-grid">
      <div class="prose">
        <h2>Чем занимаюсь</h2>
        <p>Адаптация и обучение, внутренние коммуникации, культура и управленческие команды. Обычно прихожу туда, где «что-то не так с людьми», — и обнаруживаю, что дело в процессе, в котором этим людям приходится работать.</p>
        <p>Люблю задачи, где нужно не нарисовать презентацию, а собрать механику: этапы, роли, обратную связь, метрики. И где можно честно сказать: вот что изменилось, вот чем это измерено.</p>

        <h2>Как работаю</h2>
        <ul>
          <li><b>Сначала диагностика.</b> Не «давайте проведём тренинг», а «покажите, где именно ломается».</li>
          <li><b>Потом механика.</b> Процесс, который живёт без героя-одиночки.</li>
          <li><b>Потом метрики.</b> Не «стало лучше», а что именно и насколько.</li>
          <li><b>Без пафоса.</b> Если что-то не сработало — говорю первой.</li>
        </ul>

        <h2>Этот сайт</h2>
        <p>Сад, а не блог. Заметки здесь не «опубликованы» — они растут: от ростка к черновику к зрелой мысли. Статус стоит у каждой. Мне так честнее, чем делать вид, что у меня всё сразу готово.</p>

        <h2>Связь</h2>
        <p>Почта <a href="mailto:nsbshal@gmail.com">nsbshal@gmail.com</a>, Telegram <a href="https://t.me/vestnik_adekvatnosti" target="_blank" rel="noopener">@vestnik_adekvatnosti</a>. Портфолио с кейсами — <a href="https://nsbshal-arch.github.io/portfolio-v2/" target="_blank" rel="noopener">здесь ↗</a>.</p>
      </div>
      <aside class="about-side">
        <div class="fact"><span class="f-num">20</span><span class="f-lab">лет в профессии</span></div>
        <div class="fact"><span class="f-num">1000+</span><span class="f-lab">человек в контурах, где выстраивала процессы</span></div>
        <div class="fact"><span class="f-num">3</span><span class="f-lab">направления: обучение, коммуникации, консалтинг</span></div>
      </aside>
    </div>
  </section>
</main>"""
    return shell("", "Обо мне", body, page_url="about.html")


def build_now():
    body = f"""
<main>
  <section class="page-head">
    <div class="wrap">
      <div class="kicker">сейчас · ноябрь 2026</div>
      <h1 class="page-title">Сейчас</h1>
      <p class="page-lead">Страница, которая быстро устаревает. Так и задумано: она про этот месяц, а не про «в целом».</p>
    </div>
  </section>
  <section class="section section-tight">
    <div class="wrap about-grid">
      <div class="prose">
        <h2>Делаю</h2>
        <ul>
          <li>Тестирую «Ритм» — приложение для планирования с учётом ресурса. Сейчас это прототип, который ставится на телефон. Собираю отзывы: пользуются ли им на третий день, а не на первый.</li>
          <li>Собираю портфолио: кейсы с цифрами и с честными допущениями, где цифр нет.</li>
          <li>Пишу этот сад. Медленно, по одной заметке.</li>
        </ul>

        <h2>Думаю про</h2>
        <ul>
          <li>Как мерить эффект обучения, не притворяясь, что всё измеримо.</li>
          <li>Почему забота о сотрудниках продаётся только через клиента.</li>
          <li>Где проходит граница между поддержкой и контролем — в приложениях особенно.</li>
        </ul>

        <h2>Читаю</h2>
        <p>Про корпоративную культуру и про то, как устроены сервисные команды. Ищу не «лучшие практики», а описания того, что реально ломалось и почему.</p>

        <h2>Открыто к</h2>
        <p>Проектам по адаптации, обучению и внутренним коммуникациям. И к разговору с теми, кто пробует «Ритм» — особенно если что-то не понравилось.</p>
      </div>
      <aside class="about-side">
        <div class="fact"><span class="f-num">ноя</span><span class="f-lab">2026 · последнее обновление страницы</span></div>
        <div class="fact"><a class="link-arrow" href="https://nsbshal-arch.github.io/ritm/" target="_blank" rel="noopener">Открыть «Ритм» ↗</a></div>
        <div class="fact"><a class="link-arrow" href="https://nsbshal-arch.github.io/portfolio-v2/" target="_blank" rel="noopener">Портфолио ↗</a></div>
      </aside>
    </div>
  </section>
</main>"""
    return shell("", "Сейчас", body, page_url="now.html")


def build_rss():
    items = []
    for n in sorted(NOTES, key=lambda x: x["date"], reverse=True):
        items.append(f"""    <item>
      <title>{html.escape(n['title'])}</title>
      <link>{SITE}/notes/{n['slug']}.html</link>
      <guid>{SITE}/notes/{n['slug']}.html</guid>
      <pubDate>{n['date']}T12:00:00+03:00</pubDate>
      <description>{html.escape(n['excerpt'])}</description>
    </item>""")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>{TITLE}</title>
    <link>{SITE}/</link>
    <description>Цифровой сад Надежды Добрыниной: заметки о работе с людьми, обучении и заботе.</description>
    <language>ru</language>
    <lastBuildDate>{UPDATED}T12:00:00+03:00</lastBuildDate>
{chr(10).join(items)}
  </channel>
</rss>
"""


def build_sitemap():
    urls = [("", "1.0"), ("notes.html", "0.9"), ("about.html", "0.7"), ("now.html", "0.6")]
    urls += [(f"notes/{n['slug']}.html", "0.8") for n in NOTES]
    rows = "".join(
        f"  <url><loc>{SITE}/{u}</loc><lastmod>{UPDATED}</lastmod><priority>{p}</priority></url>\n"
        for u, p in urls
    )
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{rows}</urlset>\n'


def write(rel, content):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ", rel)


if __name__ == "__main__":
    print("Собираю сад…")
    write("index.html", build_index())
    write("notes.html", build_notes_list())
    write("about.html", build_about())
    write("now.html", build_now())
    for n in NOTES:
        write(f"notes/{n['slug']}.html", build_note(n))
    write("rss.xml", build_rss())
    write("sitemap.xml", build_sitemap())
    print(f"Готово: {len(NOTES)} заметок.")
