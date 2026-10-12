# Grimoire

Every mistake worth not repeating. Types: **concept** (misunderstood idea), **procedure**
(wrong method or step), **careless** (slip), **strategy** (wrong approach, or no approach).
Conf: how sure you were, 1 to 3. Confident errors teach the most once fixed. Re-attempts at
+3, +10, +30 days; strike an entry through once it has survived the 30-day re-attempt.

| Date | Subject | Where | Error | Type | Conf | Fix | Trigger | Next |
|---|---|---|---|---|---|---|---|---|
| 2026-10-12 | analysis | ANA UE01/1 | Checked one triple, $(1,0,0)$, for the whole case "an entry is $0$" | procedure | ? | Inside a case keep the other letters free: "let $c=0$", $a,b$ arbitrary | A case split | 2026-10-15 |
| 2026-10-12 | analysis | ANA UE01/2b | $x^2\le y^2\Rightarrow x\le y$ (struck out yourself) | concept | ? | Squaring forgets the sign; compare $\lvert x\rvert $ and $\lvert y\rvert $ | An inequality between squares | 2026-10-15 |
| 2026-10-12 | analysis | ANA UE01/2b | The step $\lvert x\rvert ^2\le\lvert y\rvert ^2\Rightarrow\lvert x\rvert \le\lvert y\rvert $, which is the whole exercise, asserted without proof | strategy | ? | Prove the step that carries the problem as a lemma ($u,v\ge0$: $u^2\le v^2\Leftrightarrow u\le v$) | One step does all the work | 2026-10-15 |
| 2026-10-12 | analysis | ANA UE01/4a, 5c, 8 | Arrows between the wrong things: $\Leftrightarrow$ to a set equation, $=$ for $\Rightarrow$, $\Rightarrow$ between numbers | procedure | ? | $=$ joins objects, $\Rightarrow$ joins statements; end a set proof with "$x$ was arbitrary" | Writing a chain of arrows | 2026-10-15 |
| 2026-10-12 | analysis | ANA UE01/5c | "For $a$ real, $\frac1b\le1$": reversed, the root needs $\frac1b\ge1$; and $b=0$ forgotten | careless | ? | List every condition the formula needs, translate each into a condition on $b$ | Solving for $a$ with a root or a fraction | 2026-10-15 |
| 2026-10-12 | analysis | ANA UE01/6b | Cited injectivity for $x_1\ge x_2\Rightarrow f(x_1)\ge f(x_2)$ | concept | ? | Injectivity gives $\neq$; order comes from monotonicity | A bracket that names a reason | 2026-10-15 |
| 2026-10-12 | analysis | ANA UE01/7 | Refuted $B\Rightarrow A$ using $y=1-x$, which is part of $A$; $L_1$ never checked by plugging in | concept | ? | Refute with one point where $B$ holds and $A$ fails, here $(5,0)$; plug candidates back in | "Does the converse hold?", or a solved system | 2026-10-15 |
