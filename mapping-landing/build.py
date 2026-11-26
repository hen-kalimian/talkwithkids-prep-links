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

def adv():
    xs = [14, 28, 42, 56, 70]   # תחנות בשביל, משמאל לימין
    d = [4, 8, 2, 6, 1]         # ספרות להדגמה בלבד, לא הקוד של הכלי
    st = ''.join(f'<i class="st{" on" if i < 2 else ""}" style="left:{x}%"></i><i class="dg{" on" if i < 2 else ""}" style="left:{x}%">{d[i]}</i>' for i, x in enumerate(xs))
    return f'<div class="adv" role="img" aria-label="הילדה הולכת בשביל ביער הקסום, אוספת ספרות ומגיעה אל תיבת האוצר">{st}<img class="achest" src="img/chest-closed.png" alt=""><img class="akid" src="img/hero-girl.png" alt="" style="left:28%"></div>'

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

body = f'''
<section class="band hero"><div class="wrap">
 <img class="logo" src="img/logo.png" alt="חן קלימיאן, לדבר עם ילדים">
 <div class="heroGrid">
  <div>
   <span class="badge">לגננות, למורות ולנשות טיפול</span>
   <h1>כלי מיפוי שיעזור לך לבדוק את רמת המוכנות של ילדי הגן לקראת כיתה א' ולהעביר את המידע בצורה מקצועית להורים</h1>
  </div>
  <div class="heroImg">{adv()}</div>
  <div class="heroTxt">
   <p class="lead">שקופית אחרי שקופית: מה להגיד לילד, מה לסמן, ובסוף דוח מסודר שאפשר להגיש להורים.</p>
   <span class="gift">ובבונוס: מיפוי לכיתות א-ב-ג</span><br>
   <span class="deadline">{LAUNCH}</span>
   {cta()}
  </div>
 </div>
</div></section>

<section class="band pink"><div class="wrap narrow center">
 <h2>"נו, מה את אומרת? הוא מוכן לכיתה א'?"</h2>
 <p>אמא עומדת מולך ומחכה לתשובה. את מרגישה שיש משהו שצריך לחזק, אולי באותיות, אולי בצלילים, אולי בחשבון.</p>
 <p>ואז מתחילות השאלות שלך: מה בדיוק לבדוק? באיזה סדר? איך לרשום תוך כדי, ואיך לנסח להורים תמונה ברורה ומכבדת?</p>
 <figure class="quote card"><blockquote>"אני נתקלת בכל שנה בפערים בין הילדים ובקשיים שונים: חלקם לא מצליחים לזכור את כל האותיות, אחרים לא את סימני הניקוד והצלילים."</blockquote><figcaption>ליעד, מחנכת כיתות א'-ב', משתתפת בהכשרה שלי</figcaption></figure>
 <p class="keyline">כשיש לך מיפוי מסודר, את מגיעה לשיחה עם ההורים עם תשובות.</p>
</div></section>

<section class="band white"><div class="wrap">
 <div class="center">{ico('pencil')}<h2>ככה נראה המיפוי מגן חובה ועד אמצע כיתה א'</h2>
 <p class="sub">בכל שקופית מופיעים המשפט שאומרים לילד והפריטים לסימון: הצליח, בעזרה, לא הצליח.</p></div>
 <div class="grid g2">
  <div class="steps">{''.join(step(i + 1, t, p) for i, (t, p) in enumerate(steps))}</div>
  <div class="side">{shot('phonetic', 'משימת כתיבה לפי הצלילים', 'כתיבה לפי הצלילים, בשתי רמות')}{shot('letters', 'משימת זיהוי אותיות', 'זיהוי אותיות בהצבעה')}</div>
 </div>
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
.adv{position:relative;direction:ltr;width:100%;aspect-ratio:4/3;container-type:inline-size;overflow:hidden;border-radius:24px;border:4px solid #fff;box-shadow:0 0 0 3px var(--line),0 10px 26px rgba(184,35,107,.16);background:url(img/forest.jpg) center bottom/cover no-repeat}
.adv i{position:absolute;font-style:normal;transform:translateX(-50%)}
.adv .st{bottom:7%;width:9%;aspect-ratio:2/1;border-radius:50%;background:rgba(255,255,255,.9);border:3px solid var(--f);box-shadow:0 0 12px 4px rgba(255,255,255,.7)}.adv .st.on{background:#FBC5D6}
.adv .dg{bottom:52%;width:10cqw;height:10cqw;display:grid;place-items:center;border-radius:24%;background:#fff;border:3px solid var(--f);box-shadow:0 5px 12px rgba(184,35,107,.35);font:800 6cqw Rubik,Arial;color:var(--deep);opacity:0;transform:translateX(-50%) scale(.2);transition:opacity .3s,transform .5s cubic-bezier(.3,1.6,.5,1)}
.adv .dg.on{opacity:1;transform:translateX(-50%) scale(1)}
.adv .achest{position:absolute;left:87%;bottom:7%;width:23%;transform:translateX(-50%);filter:drop-shadow(0 0 12px rgba(255,236,170,.95))}
.adv .akid{position:absolute;bottom:8.5%;height:40%;width:auto;transform:translateX(-50%);transform-origin:50% 100%;transition:left 1.3s linear;filter:drop-shadow(0 4px 3px rgba(60,40,50,.3))}
.adv .akid.walk{animation:wk .45s ease-in-out infinite}
@keyframes wk{0%,100%{transform:translateX(-50%) rotate(-3deg)}50%{transform:translateX(-50%) translateY(-5%) rotate(3deg)}}
.wide{max-width:760px;margin:20px auto 0}.appx{margin-top:34px}.tall{max-width:560px;margin:10px auto 0}
.bon p{margin-bottom:10px}.games{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:8px}.games img{width:100%;aspect-ratio:4/3;object-fit:contain;background:#fff;border:2px solid var(--line);border-radius:12px;display:block}
@media(max-width:820px){body{font-size:17px;padding-bottom:76px}.band{padding:28px 0}.heroGrid{grid-template-columns:1fr;grid-template-areas:"t" "i" "x";gap:12px;text-align:center}.g2,.trio{grid-template-columns:1fr}
.logo{height:58px}h1{font-size:26px}
.sticky{display:block;position:fixed;bottom:10px;left:16px;right:16px;z-index:9;text-align:center;text-decoration:none;color:#fff;font:800 18px Rubik,Arial;background:linear-gradient(135deg,var(--f),var(--f2));border-radius:40px;padding:12px;box-shadow:0 6px 18px rgba(184,35,107,.35);transition:opacity .25s}.sticky.off{opacity:0;pointer-events:none}}
'''

JS = '''
/* הנפשת ההדגמה: הדמות הולכת בשביל, אוספת ספרות, והתיבה נפתחת */
(function(){var a=document.querySelector('.adv');if(!a||matchMedia('(prefers-reduced-motion: reduce)').matches)return;
var k=a.querySelector('.akid'),c=a.querySelector('.achest'),st=a.querySelectorAll('.st'),dg=a.querySelectorAll('.dg'),i;
function set(x,go){k.style.transition=go?'':'none';k.style.left=x;k.classList.toggle('walk',!!go)}
function reset(){st.forEach(function(e){e.classList.remove('on')});dg.forEach(function(e){e.classList.remove('on')});c.src='img/chest-closed.png';set('8%',false);i=0;setTimeout(next,500)}
function next(){if(i>=st.length){set('72%',true);setTimeout(function(){k.classList.remove('walk');c.src='img/chest-open.png';setTimeout(reset,2800)},1350);return}
set(st[i].style.left,true);setTimeout(function(){k.classList.remove('walk');st[i].classList.add('on');dg[i].classList.add('on');i++;setTimeout(next,800)},1350)}
new Image().src='img/chest-open.png';reset()})();
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
lost = [k for k in OV if k not in ORIG]
if lost: print('WARNING: edits without a matching text:', lost)
html = ('<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta name="robots" content="noindex,nofollow"><title>כלי מיפוי למוכנות לכיתה א\' | חן קלימיאן</title>'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500;700;800&family=Open+Sans:wght@400;600;700&display=swap" rel="stylesheet">'
        f'<style>{CSS}</style></head><body>{body}<script>{JS}</script></body></html>')
open('index.html', 'w', encoding='utf-8').write(html)
print('ok', len(html))
