// Builds mom-new/part1.html from the live /mom part1 source: adds a social-proof bar under the hero and Hen's photo in the story section.
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
const SRC = path.join(os.homedir(), 'yy', 'wg', 'mom-landing', 'part1.html');
const OUT = path.join(os.homedir(), 'yy', 'pl', 'mom-new', 'part1.html');
let s = fs.readFileSync(SRC, 'utf8');

const css = `
.proofbar{padding:22px 0!important;background:#fff}
.proofs3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;max-width:900px;margin:0 auto}
.pstat{background:var(--bg-pink);border:2px solid var(--card-line);border-radius:20px;padding:14px 10px;text-align:center}
.pstat b{display:block;font-family:Rubik,sans-serif;font-weight:800;font-size:clamp(28px,5vw,40px);color:var(--fuchsia-deep);line-height:1.1}
.pstat span{display:block;font-weight:700;font-size:17px;color:var(--ink)}
@media(max-width:640px){.proofs3{grid-template-columns:1fr;max-width:340px}.pstat{padding:10px}.pstat b{font-size:30px}}
.storyGrid{display:grid;grid-template-columns:.8fr 1.2fr;gap:28px;align-items:center}
@media(max-width:760px){.storyGrid{grid-template-columns:1fr}.storyGrid .portrait{width:min(70%,260px)}}
`;
s = s.replace('</style>', css + '</style>');

// 1. proof bar right after the hero band (first </section>)
const bar = `
<!-- הוכחה חברתית: מספרים -->
<section class="band white proofbar">
  <div class="wrap">
    <div class="proofs3">
      <div class="pstat"><b dir="ltr">+250</b><span>חברות במועדון</span></div>
      <div class="pstat"><b dir="ltr">+28,000</b><span>משפחות שרכשו את התוכניות שלי</span></div>
      <div class="pstat"><b dir="ltr">+60,000</b><span>עוקבים ברשתות</span></div>
    </div>
  </div>
</section>
`;
const i = s.indexOf('</section>') + '</section>'.length;
s = s.slice(0, i) + '\n' + bar + s.slice(i);

// 2. Hen's photo next to the story ("למה פתחתי את המועדון?")
const a = s.indexOf('<div class="wrap" style="max-width:780px">', s.indexOf('id="p1end"'));
const startTag = '<div class="wrap" style="max-width:780px">';
const end = s.indexOf('</section>', a);
let inner = s.slice(a + startTag.length, end);
inner = inner.replace(/\s*<\/div>\s*$/, '');
const head = inner.slice(0, inner.indexOf('</div>') + 6); // kicker + h2 block
const body = inner.slice(head.length);
const grid = `<div class="wrap" style="max-width:900px">${head}<div class="storyGrid"><img class="portrait" src="https://hen-kalimian.github.io/talkwithkids-prep-links/mom-new/hen.jpg" alt="חן קלימיאן, קלינאית תקשורת ואמא לארבעה" style="object-position:50% 30%"><div>${body}</div></div></div>\n`;
s = s.slice(0, a) + grid + s.slice(end);

fs.writeFileSync(OUT, s);
console.log('wrote', OUT, s.length);
