# -*- coding: utf-8 -*-
# דף הנחיתה של המיפוי בתשלום (טיוטה לאישור). הרצה: python build.py <תיקיית צילומי המסך (לא חובה)>
import os, sys, shutil
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); os.chdir(H)
os.makedirs('img', exist_ok=True)
if len(sys.argv) > 1:
    S = sys.argv[1]
    for src, dst, box in [('shots/101-step', 'vault', (0, 150, 1536, 960)), ('shots/103-step', 'phonetic', (0, 110, 1536, 760)),
                          ('shots/107-step', 'letters', (0, 110, 1536, 830)), ('shots3/32-report', 'report', (168, 24, 1368, 1150)),
                          ('shots3/51-kbB', 'kbletters', (0, 110, 1536, 750)), ('shots3/52-kbsum', 'kbsum', (0, 0, 1536, 880))]:
        Image.open(f'{S}/{src}.png').convert('RGB').crop(box).save(f'img/{dst}.jpg', quality=88)
    A = os.path.expanduser('~/training-workspace/04-output/teach-renewal')
    for n in ['target', 'printer', 'chat', 'pencil', 'key', 'gift', 'puzzle', 'folder']:
        shutil.copy(f'{A}/art/{n}.png', f'img/{n}.png')
    Image.open(f'{A}/img/live_27.jpg').convert('RGB').save('img/hen.jpg', quality=90)
    shutil.copy(os.path.expanduser('~/yy/wg/mapping/img/logo.png'), 'img/logo.png')

def shot(n, alt, cap=''):
    w, h = Image.open(f'img/{n}.jpg').size
    c = f'<figcaption>{cap}</figcaption>' if cap else ''
    return f'<figure class="shot"><img src="img/{n}.jpg" alt="{alt}" width="{w}" height="{h}">{c}</figure>'

def ico(n):
    return f'<img class="ico" src="img/{n}.png" alt="">'

def cta(t='אני רוצה את כלי המיפוי'):
    return f'<a class="btn" href="#offer">{t}</a>'

def vault():
    keys = ''.join(f'<i class="k" data-d="{n}">{n}</i>' for n in [1, 2, 3, 4, 5, 6, 7, 8, 9])
    keys += '<i class="k del">⌫</i><i class="k" data-d="0">0</i><i class="k ok">✓</i>'
    return ('<div class="vh" role="img" aria-label="מקישים קוד בן 5 ספרות, תיבת האוצר נפתחת, ויוצאת ממנה מתנה עם קונפטי">'
            f'<div class="vsl">{"<b></b>" * 5}</div><div class="vbox2"><img class="vch" src="img/chest-closed.png" alt=""><img class="vgf" src="img/hgift.png" alt=""></div>'
            f'<div class="vkp">{keys}</div><div class="vcf"></div></div>')

def step(i, t, p):
    return f'<div class="step"><span class="num">{i}</span><div><h3>{t}</h3><p>{p}</p></div></div>'

LAUNCH = 'מחיר השקה עד חנוכה'
steps = [
    ('מתחילות בהורים', 'ממלאים פעם אחת את פרטי הילד, ורושמים מה עלה בשיחה עם ההורים. הפרטים עוברים לבד לדוח המסכם.'),
    ('כתיבת השם', 'את רואה אילו אותיות הילד מזהה ומשיים, איך הוא אוחז בכלי הכתיבה ומאיזה כיוון הוא כותב.'),
    ('כתיבה לפי הצלילים', 'בוחרים רמה, הילד רואה איורים וכותב את מה שהוא שומע. את מסמנת צליל פותח, צליל סוגר וקשר בין אות לצליל.'),
    ('חשבון', 'ספירה, מנייה, כתיבת מספרים, השוואת כמויות ותרגילי חיבור.'),
    ('אותיות בשלושה שלבים', 'כתיבה בהכתבה, שיום וזיהוי בהצבעה. כל אות מקבלת את הסימון שלה.'),
    ('לומדים משהו חדש', 'את מלמדת בזמן אמת, ובודקת אם הילד מבין, מיישם, זוכר ומתקן את עצמו.'),
]

PAIR_SHOTS = [('ex-name', 'דוגמה למשימת כתיבת השם, עם סימון ההיגדים', 'כתיבת השם: הילד כותב, ואת מסמנת'),
              ('ex-sounds', 'משימת כתיבה לפי הצלילים', 'כתיבה לפי הצלילים, בשתי רמות'),
              ('ex-teach', 'בחירת משחק הלמידה בתוך כלי המיפוי', 'בדיקת יכולת למידה: בוחרים מה ללמד')]

def pair(i):
    two = ''.join(step(j + 1, *steps[j]) for j in (2 * i, 2 * i + 1))
    return f'<div class="grid g2 mid pair"><div class="steps">{two}</div>{shot(*PAIR_SHOTS[i])}</div>'

body = f'''
<section class="band hero"><div class="wrap">
 <img class="logo" src="img/logo.png" alt="חן קלימיאן, לדבר עם ילדים">
 <div class="heroGrid">
  <div>
   <span class="badge">לגננות, למורות ולנשות טיפול</span>
   <h1>כלי המיפוי שיעזור לך למלא קבוצות הכנה לכיתה א' <span class="h1b">ובהדרכת הבונוס: איך להפוך את פגישת המיפוי לפגישה שבסופה ההורים רוצים להירשם</span></h1>
  </div>
  <div class="heroImg">{vault()}</div>
  <div class="heroTxt">
   <p class="subh">מיפוי דיגיטלי ומשחקי שיעזור לך לבדוק בקלות את רמת המוכנות של ילדי הגן ולהעביר את המידע להורים בצורה מקצועית</p>
   <p class="lead">שקופית אחרי שקופית: מה להגיד לילד, מה לסמן, ובסוף דוח מסודר שאפשר להגיש להורים.</p>
   <span class="gift">ובבונוס: מיפוי לכיתות א-ב-ג</span><br>
   <span class="deadline">{LAUNCH}</span>
   {cta()}
  </div>
 </div>
</div></section>

<section class="band pink" id="case"><div class="wrap narrow center">
 <h2>איך עדן סגרה 20 מפגשים אחרי מפגש מיפוי</h2>
 <p>עדן גבאי, קלינאית ומשתתפת בהכשרה שלי, קיבלה אליה אמא ובת למפגש מיפוי.</p>
 <p>המיפוי היה מוצלח מאוד: האמא התרשמה, והילדה נהנתה מאוד.</p>
 <p>ובזכות ההדרכה שלי, האמא נרשמה ל-20 מפגשים.</p>
 <p><b>הנה מה שהיא כתבה לי:</b></p>
 <img class="wa" src="img/eden-lines2.jpg" alt="הודעה שעדן שלחה לי: בזכות ההדרכה שלך היא נרשמה ל-20 מפגשים" width="1320" height="765">
 <p class="keyline">ככה מפגש מיפוי אחד יכול להפוך לתהליך שלם</p>
</div></section>

<section class="band white"><div class="wrap">
 <div class="center">{ico('pencil')}<h2>ככה נראה המיפוי מגן חובה ועד אמצע כיתה א'</h2>
 <p class="sub">בכל שקופית מופיעים המשפט שאומרים לילד והפריטים לסימון: הצליח, בעזרה, לא הצליח.</p></div>
 <div class="pairs">{''.join(pair(i) for i in range(3))}</div>
 {cta()}
</div></section>

<section class="band mint"><div class="wrap narrow center">
 {ico('key')}<h2>בשביל הילד זו הרפתקה עם כספת</h2>
 <p>בתחילת המפגש מחכה לו כספת עם הפתעה. על כל משימה שעשיתם יחד הוא מקבל ספרה, ובסוף מקיש את הקוד ופותח אותה.</p>
 <p class="keyline">הילד מתקדם בשביל הספרה הבאה, ואת רואה מה הוא יודע.</p>
 <div class="wide">{shot('journey', 'בחירת דמות והשביל ביער הקסום בתוך כלי המיפוי', 'כך זה נראה בכלי: הילד בוחר דמות ויוצא לדרך')}</div>
</div></section>

<section class="band white"><div class="wrap">
 <div class="grid g2 mid">
  <div>
   {ico('printer')}<h2>ובסוף, דוח שנעים לך להגיש להורים</h2>
   <p>הסימונים וההערות שלך מתכנסים לדף סיכום אחד:</p>
   <ul class="ticks"><li>נקודות חוזק</li><li>מוקדי קושי</li><li>מטרות ראשוניות</li><li>המלצות להורים</li><li>המלצות להמשך</li></ul>
   <p>את יכולה להדפיס, לשמור כ-PDF או כתמונה בעמוד A4, להעתיק הודעה מסכמת להורים לוואטסאפ או למייל, ולפתוח תבנית דוח להורים.</p>
  </div>
  <div>{shot('report', 'דוגמה לדוח סיכום מיפוי', 'דוגמה לדוח, עם ילדה בדויה')}</div>
 </div>
 <div class="center appx"><h3>והנספח: כל המשימות שהילד ביצע</h3>
 <p class="sub">הכתיבה של הילד, הסימונים וההערות שלך, בדף אחד.</p>
 <div class="tall">{shot('appendix', 'דוגמה לנספח עם הכתיבה של הילד והסימונים', 'דוגמה מתוך מיפוי שמילאתי, עם שם בדוי')}</div></div>
 {cta()}
</div></section>

<section class="band pink" id="grow"><div class="wrap narrow center">
 {ico('chat')}<h2>המיפוי הוא כלי השיווק החזק ביותר שלנו</h2>
 <p class="lead">והוא עוזר לנו למלא קבוצות הכנה לכיתה א'.</p>
 <div class="steps grow">{step(1, 'נזמין את ההורים למפגש מיפוי', 'מפגש שבו הילד יוצא להרפתקה, וההורים מכירים אותנו ואת הדרך שבה אנחנו עובדות.')}{step(2, 'ההורים יגלו את סוד הקסם שלנו', 'הם יראו ילד שנהנה ומשתף פעולה, ויקבלו תמונה ברורה ומקצועית על מה שהוא כבר יודע ומה השלב הבא שלו.')}{step(3, 'יתאהבו בשיטה', 'וכך ירצו להירשם לקבוצה, ורק אלינו.')}</div>
 <p class="keyline">ובהדרכת הבונוס תגלי איך להפוך את פגישת המיפוי לפגישה שבסופה ההורים רוצים להירשם לקבוצה</p>
 {cta()}
</div></section>

<section class="band sky"><div class="wrap">
 <div class="center">{ico('gift')}<span class="gift">בונוס</span>
 <h2>כלי מיפוי לילדי כיתות א-ב-ג שעדיין לא רכשו קריאה שוטפת, עם סיכום ומטרות מאורגנות לך ולהורים</h2></div>
 <div class="wide">{shot('nonsense', 'משימת קריאת מילות תפל במיפוי לילדי כיתות א עד ג', 'קריאת מילות תפל: ככה רואים איך הילד קורא בלי לנחש')}</div>
 <div class="grid g2">
  <div>{shot('kbletters', 'שיום אותיות במיפוי כיתות א עד ג', 'מתחילים בכתיב, וממשיכים לפי הקושי')}</div>
  <div>{shot('kbsum', 'סיכום ומסקנות במיפוי כיתות א עד ג', 'סיכום, מטרות והמלצות במקום אחד')}</div>
 </div>
 <div class="trio"><span>{ico('puzzle')}<em>כתיב פונטי ואותיות</em></span><span>{ico('target')}<em>הברות לפי סימני ניקוד ומילות תפל</em></span><span>{ico('chat')}<em>כתיבה עם ניקוד וקריאה בקול</em></span></div>
</div></section>

<section class="band mint"><div class="wrap">
 <div class="center">{ico('key')}<span class="gift">ועוד בונוסים</span><h2>מה מחכה לך יחד עם המיפוי</h2></div>
 <div class="grid g2">
  <div class="card bon center"><h3>שיעור בן 90 דקות: "מיפוי 5 השלבים בשיטת הכספת"</h3>
   <p>בשיעור אני מסבירה איך להשתמש במיפוי, ואיך להשתמש בו גם כדי לגייס את ההורים לרצות לעבוד איתנו ולהירשם לקבוצות הכנה לכיתה א' או לשיעורים פרטיים.</p>
   <p class="keyline">ונלמד את סודות השיווק והמכירה</p></div>
  <div class="card bon center"><h3>2 משחקים דיגיטליים להקניית חומר חדש בשיטת "קוראים בקלות"</h3>
   <p>לחלק החמישי של המפגש: לומדים את האות ג או ה, או קמץ ופתח. המשחק נפתח בתוך המיפוי, ואחר כך מסמנים אם הילד הבין והטמיע. אפשר גם ללמד בלי משחק דיגיטלי.</p>
   <div class="games"><img src="img/teach-g.jpg" alt="משחק האות ג"><img src="img/teach-h.jpg" alt="משחק האות ה"><img src="img/teach-kp.jpg" alt="משחק קמץ ופתח"></div></div>
 </div>
 {cta()}
</div></section>

<section class="band pink"><div class="wrap">
 <div class="grid g2 mid">
  <div class="heroPhoto">{shot('hen', 'חן קלימיאן')}</div>
  <div>
   <h2>נעים להכיר, אני חן</h2>
   <p>אני חן קלימיאן, קלינאית תקשורת ומדריכת הורים, ואמא לארבעה. אני עובדת עם ילדים מאז 2014, והכשרתי מאות נשות חינוך וטיפול להכנה לכיתה א'.</p>
   <p>בניתי את כלי המיפוי לפי שיטת "קוראים בקלות", כדי שתהיה לך דרך מסודרת לבדוק, לרשום ולהסביר להורים מה הילד כבר יודע ומה השלב הבא שלו.</p>
  </div>
 </div>
</div></section>

<section class="band white" id="offer"><div class="wrap">
 <div class="card offer center">
  {ico('folder')}<h2>מה את מקבלת</h2>
  <ul class="ticks">
   <li>מיפוי מודרך מגן חובה ועד אמצע כיתה א'</li>
   <li>בונוס: מיפוי מסוף כיתה א' ועד כיתה ג'</li>
   <li>דוח סיכום עם חוזקות, קשיים, מטרות והמלצות</li>
   <li>נספח עם כל המשימות שהילד ביצע</li>
   <li>שיעור בן 90 דקות: "מיפוי 5 השלבים בשיטת הכספת"</li>
   <li>2 משחקים דיגיטליים להקניית חומר חדש בשיטת "קוראים בקלות"</li>
   <li>הודעה מסכמת ותבנית דוח להורים</li>
   <li>שמירה של מיפויים קודמים, להמשך ולהשוואה</li>
  </ul>
  <span class="deadline">{LAUNCH}</span>
  <p class="price"><b>39</b> ₪</p>
  <button type="button" class="btn" id="buy">אני רוכשת עכשיו</button>
  <p class="buynote" id="buynote" hidden>זו טיוטה: כפתור הרכישה יחובר לתשלום אחרי האישור.</p>
 </div>
</div></section>

<section class="band mint"><div class="wrap narrow faq">
 <h2 class="center">שאלות שעולות</h2>
 <details><summary>לאילו גילים הכלי מתאים?</summary><p>המיפוי הראשון מיועד לגן חובה ועד אמצע כיתה א'. מיפוי הבונוס מיועד לילדים מסוף כיתה א' ועד כיתה ג' שעדיין לא רכשו קריאה שוטפת.</p></details>
 <details><summary>אני אמא, האם אפשר להעביר את זה לילד שלי?</summary><p>הכלי נבנה עבור נשות חינוך וטיפול שעובדות עם יותר מילד אחד. אין איסור לרכוש את המיפוי אם את לא מגיעה מהתחום, אך אין צורך לעשות זאת.</p></details>
 <details><summary>איזה ציוד צריך?</summary><p>מחשב, טאבלט או טלפון עם אינטרנט. לכתיבה מומלץ טאבלט עם עט ייעודי, ואפשר גם לכתוב בדף עם עיפרון ולצלם.</p></details>
 <details><summary>חייבים לעבור את כל המשימות במפגש אחד?</summary><p>אפשר לעצור בכל רגע, לשמור ולהמשיך מאותה שקופית בפעם הבאה.</p></details>
 <details><summary>איפה נשמרים המיפויים?</summary><p>המיפויים נשמרים במכשיר, ובהתחברות אפשר לשמור אותם גם בחשבון. כדאי לשמור לעצמך כל מיפוי גם כ-PDF או כתמונה.</p></details>
 <details><summary>זה אבחון?</summary><p>זה מיפוי שנותן לך תמונת מצב לעבודה ולשיחה עם ההורים. כשעולה צורך, אפשר לסמן בסיכום המלצה להערכה מקצועית.</p></details>
 {cta()}
</div></section>
<footer>כל הזכויות שמורות לחן קלימיאן | לדבר עם ילדים</footer>
<a class="sticky" href="#offer">אני רוצה את כלי המיפוי</a>
'''

CSS = '''
:root{--pink-bg:#FEF6F5;--card:#FDE1EA;--line:#FBC5D6;--mint:#EEF8F3;--sky:#F1F8FD;--ink:#27413C;--soft:#4f6660;--f:#EF406E;--f2:#F27A9B;--deep:#B8236B}
*{box-sizing:border-box}html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:#fff;color:var(--ink);font-family:"Open Sans",Assistant,Arial,sans-serif;font-size:18px;line-height:1.7;overflow-x:hidden}
h1,h2,h3{font-family:Rubik,Assistant,Arial,sans-serif;line-height:1.28;margin:0 0 10px}
h1{font-size:clamp(27px,3.6vw,40px);font-weight:800}h2{font-size:clamp(23px,3.4vw,33px);font-weight:800}h3{font-size:19px;font-weight:800;margin:0}
p{margin:0 0 12px}.wrap{max-width:1080px;margin:0 auto;padding:0 18px}.narrow{max-width:760px}.center{text-align:center}
.band{padding:40px 0}.pink{background:linear-gradient(180deg,#FEF6F5,#FDE8EC)}.mint{background:var(--mint)}.sky{background:var(--sky)}
.hero{padding-top:14px;background:linear-gradient(180deg,#fff,#FEF0F2)}.logo{display:block;height:74px;width:auto;margin:0 auto 14px}
.heroGrid{display:grid;grid-template-columns:1.1fr .9fr;grid-template-areas:"t i" "x i";gap:0 30px;align-items:center}.heroGrid>div:first-child{grid-area:t;align-self:end}.heroImg{grid-area:i}.heroTxt{grid-area:x;align-self:start}
.badge,.gift,.deadline{display:inline-block;font-weight:800;border-radius:30px;padding:3px 16px;margin:0 0 12px;font-size:16px}
.badge{background:#fff;border:2px solid var(--line);color:var(--deep)}.gift{background:var(--deep);color:#fff}.deadline{background:var(--card);color:var(--deep)}
.lead{font-size:clamp(18px,2.2vw,21px);font-weight:700;color:var(--soft)}
.btn{display:block;width:fit-content;max-width:100%;margin:16px auto 0;background:linear-gradient(135deg,var(--f),var(--f2));color:#fff;border:0;text-decoration:none;text-align:center;font:800 20px Rubik,Arial,sans-serif;padding:14px 36px;border-radius:16px;box-shadow:0 8px 22px rgba(239,64,110,.28);cursor:pointer}
.shot{margin:0}.shot img{width:100%;height:auto;display:block;border-radius:20px;border:4px solid #fff;box-shadow:0 0 0 3px var(--line),0 10px 26px rgba(184,35,107,.12)}
.shot figcaption{text-align:center;font-size:16px;font-weight:700;color:var(--soft);padding-top:10px}
.grid{display:grid;gap:24px}.grid>*{min-width:0}.g2{grid-template-columns:1fr 1fr;margin-top:18px}.mid{align-items:center}
.card{background:#fff;border:2px solid var(--line);border-radius:22px;padding:22px 24px;box-shadow:0 6px 18px rgba(184,35,107,.08)}
.quote{margin:22px auto}.quote blockquote{margin:0 0 6px;font-weight:700;font-size:19px}.quote figcaption{color:var(--deep);font-size:16px}
.keyline{font:800 clamp(20px,2.8vw,25px) Rubik,Arial,sans-serif;color:var(--deep);line-height:1.45;margin:16px 0 0}
.ico{display:block;height:64px;width:auto;margin:0 auto 8px}.sub{color:var(--soft)}
.steps{display:grid;gap:10px;align-content:start}.step{display:flex;gap:12px;background:var(--pink-bg);border:2px solid var(--line);border-radius:18px;padding:12px 16px}.step p{margin:0;font-size:16px;line-height:1.6;color:var(--soft)}
.num{flex:none;width:34px;height:34px;border-radius:50%;background:var(--f);color:#fff;font:800 17px Rubik,Arial;display:flex;align-items:center;justify-content:center}
.side{display:grid;gap:18px;align-content:center}
.ticks{list-style:none;padding:0;margin:10px 0 16px;display:grid;gap:8px;text-align:right}.ticks li{position:relative;background:#FFF2F5;border-radius:14px;padding:8px 40px 8px 14px;font-weight:700}.ticks li:before{content:"\\2713";position:absolute;right:14px;top:8px;color:var(--f);font-weight:800}
.trio{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:22px}.trio em{font-style:normal;display:block}.trio span{background:#fff;border:2px solid var(--line);border-radius:20px;padding:14px;text-align:center;font-weight:800;color:var(--deep)}
.heroPhoto{max-width:420px;width:100%;margin:0 auto}
.offer{max-width:600px;margin:0 auto;border-width:3px;background:linear-gradient(180deg,#fff,#FEF6F5)}
.price{font:800 30px Rubik,Arial;color:var(--deep);margin:0;line-height:1.2}.price b{font-size:64px}
.buynote{margin-top:12px;font-size:15px;color:var(--deep);font-weight:700}
.faq details{background:#fff;border:2px solid var(--line);border-radius:16px;padding:12px 18px;margin-bottom:10px}.faq summary{font:800 18px Rubik,Arial;cursor:pointer}.faq details p{margin:8px 0 0}
footer{text-align:center;font-size:14px;color:var(--soft);padding:20px 12px}
.sticky{display:none}
.vh{position:relative;direction:ltr;width:100%;aspect-ratio:4/3;container-type:inline-size;overflow:hidden;border-radius:24px;border:4px solid #fff;box-shadow:0 0 0 3px var(--line),0 10px 26px rgba(184,35,107,.16);background:linear-gradient(180deg,rgba(255,255,255,.35),rgba(254,246,245,.55)),url(img/forest.jpg) center bottom/cover no-repeat}
.vh i{font-style:normal}
.vsl{position:absolute;top:4%;left:0;right:0;display:flex;justify-content:center;gap:1.8cqw;z-index:3;transition:opacity .4s}.vh.open .vsl{opacity:0}
.vsl b{width:9.5cqw;height:11cqw;display:grid;place-items:center;border-radius:2.4cqw;background:rgba(255,255,255,.93);border:3px solid var(--line);font:800 6.4cqw Rubik,Arial;color:var(--deep);transition:transform .25s,background .25s}
.vsl b.on{border-color:var(--f);background:#FDE1EA;transform:scale(1.08)}.vsl.win b{background:#d8f3e6;border-color:#59b98e;color:#1e6b4b}
.vbox2{position:absolute;left:5%;bottom:6%;width:48%;height:66%;transition:left .7s ease,width .7s ease,height .7s ease}
.vch{position:absolute;left:50%;bottom:0;width:100%;max-height:100%;object-fit:contain;object-position:center bottom;transform:translateX(-50%);filter:drop-shadow(0 0 14px rgba(255,236,170,.95))}
.vgf{position:absolute;left:50%;bottom:24%;width:34%;opacity:0;transform:translate(-50%,0) scale(.15);filter:drop-shadow(0 8px 10px rgba(184,35,107,.35))}
.vkp{position:absolute;right:5%;bottom:6%;width:36%;display:grid;grid-template-columns:repeat(3,1fr);gap:1.6cqw;padding:2.2cqw;border-radius:4cqw;background:rgba(255,255,255,.93);border:3px solid var(--line);transition:opacity .4s,transform .5s}
.vkp .k{height:9.6cqw;display:grid;place-items:center;border-radius:2.4cqw;background:#fff;border:2px solid var(--line);font:800 5cqw Rubik,Arial;color:var(--deep);transition:transform .15s,background .15s}
.vkp .k.ok{background:var(--f);border-color:var(--f);color:#fff}.vkp .k.del{background:#e8f7f0;border-color:#9fe3c8;color:#2a7f62}
.vkp .k.tap{background:#FBC5D6;transform:scale(.86);box-shadow:0 0 0 1.4cqw rgba(239,64,110,.3)}
.vh.open .vkp{opacity:0;transform:translateX(30%)}
.vh.open .vbox2{left:14%;width:72%;height:70%}
.vh.open .vch{animation:vpop .8s cubic-bezier(.3,1.5,.5,1) both}
@keyframes vpop{0%{transform:translateX(-50%) scale(.75) rotate(-4deg)}100%{transform:translateX(-50%) scale(1)}}
.vh.open .vgf{animation:vgf 1.2s .35s cubic-bezier(.3,1.35,.5,1) forwards}
@keyframes vgf{0%{opacity:0;transform:translate(-50%,0) scale(.15)}25%{opacity:1}100%{opacity:1;transform:translate(-50%,-78%) scale(1) rotate(-5deg)}}
.vh.shake .vbox2{animation:vsh .45s ease-in-out}
@keyframes vsh{0%,100%{transform:rotate(0)}20%{transform:rotate(-4deg)}40%{transform:rotate(4deg)}60%{transform:rotate(-3deg)}80%{transform:rotate(3deg)}}
.vcf{position:absolute;inset:0;pointer-events:none;z-index:4}
.vcf i{position:absolute;top:-6%;width:1.8cqw;height:3cqw;border-radius:.4cqw;animation:vfall linear forwards}
@keyframes vfall{to{top:106%;transform:rotate(700deg)}}
.grow{text-align:right;margin-top:18px}.grow .step{background:#fff}
.h1b{display:block;margin-top:8px;font-size:.74em;line-height:1.35;color:var(--deep);text-wrap:balance}.subh{font:700 clamp(18px,2.2vw,22px)/1.5 Rubik,Arial,sans-serif;color:var(--ink);margin-bottom:8px}.heroTxt .lead{font-size:clamp(16px,1.7vw,18px);font-weight:600}
@media(min-width:821px) and (max-height:720px){.logo{height:52px;margin-bottom:6px}.hero{padding-top:6px;padding-bottom:20px}}
.wa{display:block;width:100%;max-width:600px;height:auto;margin:6px auto 0;box-shadow:0 10px 26px rgba(184,35,107,.16)}
.pairs{display:grid;gap:30px;margin-top:18px}.pair{margin-top:0}.pair .shot{max-width:520px;width:100%;justify-self:center}
.wide{max-width:760px;margin:20px auto 0}.appx{margin-top:34px}.tall{max-width:560px;margin:10px auto 0}
.bon p{margin-bottom:10px}.games{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:8px}.games img{width:100%;aspect-ratio:4/3;object-fit:contain;background:#fff;border:2px solid var(--line);border-radius:12px;display:block}
@media(max-width:820px){.vh{max-width:520px;margin:0 auto}body{font-size:17px;padding-bottom:76px}.band{padding:28px 0}.heroGrid{grid-template-columns:1fr;grid-template-areas:"t" "i" "x";gap:12px;text-align:center}.g2,.trio{grid-template-columns:1fr}
.logo{height:58px}h1{font-size:26px}
.sticky{display:block;position:fixed;bottom:10px;left:16px;right:16px;z-index:9;text-align:center;text-decoration:none;color:#fff;font:800 18px Rubik,Arial;background:linear-gradient(135deg,var(--f),var(--f2));border-radius:40px;padding:12px;box-shadow:0 6px 18px rgba(184,35,107,.35);transition:opacity .25s}.sticky.off{opacity:0;pointer-events:none}}
'''

JS = '''
/* הנפשת הפתיחה: מקישים קוד בן 5 ספרות, התיבה נפתחת, יוצאת מתנה וקונפטי. בלי סאונד */
(function(){var a=document.querySelector('.vh');if(!a)return;
var sl=a.querySelector('.vsl'),box=sl.children,ch=a.querySelector('.vch'),cf=a.querySelector('.vcf'),code=[2,4,8,1,6],i;  /* ספרות להדגמה בלבד, לא הקוד של הכלי */
new Image().src='img/chest-open.png';
function key(s){var k=a.querySelector(s);k.classList.add('tap');setTimeout(function(){k.classList.remove('tap')},280)}
function reset(){a.classList.remove('open','shake');sl.classList.remove('win');cf.textContent='';ch.src='img/chest-closed.png';[].forEach.call(box,function(b){b.textContent='';b.className=''});i=0;setTimeout(next,900)}
function next(){if(i<5){key('.k[data-d="'+code[i]+'"]');box[i].textContent=code[i];box[i].className='on';i++;setTimeout(next,620);return}
key('.k.ok');setTimeout(function(){sl.classList.add('win');a.classList.add('shake');setTimeout(open,550)},300)}
function open(){a.classList.remove('shake');ch.src='img/chest-open.png';a.classList.add('open');setTimeout(party,400);setTimeout(reset,5200)}
function party(){var c=['#EF406E','#FBC5D6','#9fe3c8','#9ad7f5','#ffd966','#c9a7f0'],h='';for(var n=0;n<70;n++)h+='<i style="left:'+Math.random()*100+'%;background:'+c[n%6]+';animation-delay:'+(Math.random()*1.4).toFixed(2)+'s;animation-duration:'+(1.8+Math.random()*1.6).toFixed(2)+'s"></i>';cf.innerHTML=h}
if(matchMedia('(prefers-reduced-motion: reduce)').matches){[].forEach.call(box,function(b,n){b.textContent=code[n];b.className='on'});ch.src='img/chest-open.png';a.classList.add('open');return}
reset()})();
var b=document.getElementById('buy');b.onclick=function(){document.getElementById('buynote').hidden=false};
var s=document.querySelector('.sticky'),seen=new Set();
var io=new IntersectionObserver(function(es){es.forEach(function(e){e.isIntersecting?seen.add(e.target):seen.delete(e.target)});upd()});
function upd(){s.classList.toggle('off',seen.size>0||scrollY<500)}
addEventListener('scroll',upd,{passive:true});upd();
document.querySelectorAll('.btn,#offer').forEach(function(e){io.observe(e)});
'''
body = body.replace("כיתה א'", "כיתה א'")
# --- עריכת טקסט: לכל קטע טקסט מפתח קבוע, והתיקונים של חן (texts.json) גוברים על הטקסט המקורי
import re, json, hashlib
OV = json.load(open('texts.json', encoding='utf-8')) if os.path.exists('texts.json') else {}
ORIG = {}
def key_el(m):
    tag, attr, inner = m.group(1), m.group(2), m.group(3)
    if tag == 'span' and not re.search(r'class="(badge|gift|deadline)"', attr): return m.group(0)
    if tag == 'a' and not re.search(r'class="(btn|sticky)"', attr): return m.group(0)
    if 'id="buynote"' in attr or not inner.strip(): return m.group(0)
    k = 't' + hashlib.md5(inner.encode('utf-8')).hexdigest()[:10]
    ORIG[k] = inner
    return f'<{tag}{attr} data-k="{k}">{OV.get(k, inner)}</{tag}>'
body = re.sub(r'<(h1|h2|h3|p|li|summary|figcaption|blockquote|button|footer|em|span|a)((?:\s[^>]*)?)>((?:(?!<\1[\s>]|<img|<div|<span class="num).)*?)</\1>', key_el, body, flags=re.S)
json.dump(ORIG, open('orig.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
RETIRED = {'t6e530d13c4', 't529cbbc684'}  # הכותרת הארוכה פוצלה לפי בקשת חן לכותרת ולכותרת משנה
lost = [k for k in OV if k not in ORIG and k not in RETIRED]
if lost: print('WARNING: edits without a matching text:', lost)
html = ('<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta name="robots" content="noindex,nofollow"><title>כלי מיפוי למוכנות לכיתה א\' | חן קלימיאן</title>'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500;700;800&family=Open+Sans:wght@400;600;700&display=swap" rel="stylesheet">'
        f'<style>{CSS}</style></head><body>{body}<script>{JS}</script></body></html>')
open('index.html', 'w', encoding='utf-8').write(html)
print('ok', len(html))
