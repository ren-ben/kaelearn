---
date: 2026-10-12
source: Notability "ANA Übung 1" (handwritten, all eight solved before the debrief; statements reconstructed from the answers)
problems:
  - source: ANA UE01/1
    solved: self
    idea: Exhaustion over two elements; any case containing a 0 collapses by the neutral element.
  - source: ANA UE01/2
    solved: self
    idea: The difference is a square; t -> t^2 is strictly increasing on [0, inf), so x^2 <= y^2 iff |x| <= |y|.
  - source: ANA UE01/3
    solved: self
    idea: On [0,1], t^2 <= t, so the p-balls grow with p: diamond in disc in square.
  - source: ANA UE01/4
    solved: self
    idea: Preimages are defined by a condition on x, so union becomes "or".
  - source: ANA UE01/5
    solved: self
    idea: Surjective and injective are questions about solving f(a) = b, with a in the domain, b in the codomain.
  - source: ANA UE01/6
    solved: self
    idea: Strictly increasing maps preserve, hence reflect, order (total order); reflecting order is "inverse increasing".
  - source: ANA UE01/7
    solved: self
    idea: Solving is a chain of implications that yields candidates; the converse makes them solutions.
  - source: ANA UE01/8
    solved: self
    idea: Factor out what the target contains, (n+1)^2.
next: 2026-10-19          # variants due; after a success +30 days, done after the second
---
## Variant 01 (of ANA UE01/1)
In $\mathbb{Z}_3$: $1\cdot1=1$ and $2\cdot2=4\equiv1$, so $1^{-1}=1$, $2^{-1}=2$. In $\mathbb{Z}_4$: $2\cdot0=0$,
$2\cdot1=2$, $2\cdot2=4\equiv0$, $2\cdot3=6\equiv2$; never $1$, so $2$ has no inverse and (inv ·) fails. Also
$2\cdot2=0$ with $2\neq0$, which no field allows (multiply $ab=0$ by $a^{-1}$ to get $b=0$).

## Variant 02 (of ANA UE01/2)
$(|x|+|y|)^2=x^2+2|x||y|+y^2\ge x^2+2xy+y^2=(x+y)^2$, because $|x||y|=|xy|\ge xy$. So $|x+y|^2\le(|x|+|y|)^2$. Both
$|x+y|$ and $|x|+|y|$ are $\ge0$, so the lemma ($u,v\ge0$: $u^2\le v^2\Rightarrow u\le v$) gives $|x+y|\le|x|+|y|$.
The $\ge0$ is used exactly in that last step.

## Variant 03 (of ANA UE01/3)
$B$: diamond with corners $(\pm2,0)$, $(0,\pm1)$. $C$: ellipse with semi-axes $2$ and $1$. Substitute $u=x/2$, $v=y$:
$B=\{|u|+|v|\le1\}$, $C=\{u^2+v^2\le1\}$, so $B\subseteq C$ by Problem 03 ($|u|,|v|\le1\Rightarrow u^2\le|u|$, $v^2\le|v|$).
Not $C\subseteq B$: $(x,y)=(\sqrt2,\frac{1}{\sqrt2})$ has $x^2+4y^2=2+2=4$ but $|x|+2|y|=2\sqrt2>2$.

## Variant 04 (of ANA UE01/4)
Let $x\in M$. $x\in f^{-1}(C\setminus D)\Leftrightarrow f(x)\in C\wedge f(x)\notin D\Leftrightarrow x\in f^{-1}(C)\wedge
x\notin f^{-1}(D)\Leftrightarrow x\in f^{-1}(C)\setminus f^{-1}(D)$; $x$ arbitrary, so the sets are equal.
$h^{-1}([0,3])=\{x: 1\le x^2\le4\}=[-2,-1]\cup[1,2]$. $h([-1,2])=[-1,3]$: $x^2\in[0,4]$ there, so $h(x)\in[-1,3]$; and
every $t\in[-1,3]$ is $h(\sqrt{t+1})$ with $\sqrt{t+1}\in[0,2]$.

## Variant 05 (of ANA UE01/5)
$k_1$: never takes the value $1$ ($\frac{x+1}{x-1}=1\Leftrightarrow x+1=x-1$, impossible), so it maps into
$\mathbb{R}\setminus\{1\}$. Solve $\frac{a+1}{a-1}=b$: $a(b-1)=b+1$, $a=\frac{b+1}{b-1}$ for $b\neq1$, and this $a\neq1$.
So bijective, and $k_1^{-1}=k_1$ (check: $k_1(k_1(x))=\frac{2x/(x-1)}{2/(x-1)}=x$).
$k_2$: maps $(0,\infty)$ into $(0,1)$; injective ($a^2=b^2$, $a,b>0$); surjective ($b\in(0,1)\Rightarrow
a=\sqrt{\frac1b-1}>0$). Bijective, $k_2^{-1}(b)=\sqrt{\frac1b-1}$. Contrast with $f_3$: same rule, different domain and
codomain.

## Variant 06 (of ANA UE01/6)
Strictly decreasing $\Rightarrow$ injective (Problem 06a); surjective by hypothesis; so $f^{-1}:J\to I$ exists. Let
$y_1<y_2$ in $J$, $x_i=f^{-1}(y_i)$. Suppose $x_1\le x_2$. If $x_1=x_2$, then $y_1=y_2$ (f is a function). If
$x_1<x_2$, then $y_1=f(x_1)>f(x_2)=y_2$ (f strictly decreasing). Both contradict $y_1<y_2$, so $x_1>x_2$: $f^{-1}$
is strictly decreasing. Grade the named hypotheses: function, decreasing, total order.

## Variant 07 (of ANA UE01/7)
(a) $A\Rightarrow B$: $x^2-y^2=(x-y)(x+y)=x+y=5$, with $x-y=1$: $x=3$ (and $y=2$). $B\Rightarrow A$ false: $(3,0)$.
Solution set on $\mathbb{R}^2$: candidates $(3,2)$; check $3-2=1$, $9-4=5$, so $\{(3,2)\}$. On $\{y<0\}$: $\emptyset$.
(b) Squaring: $x+2=x^2$, $x=2$ or $x=-1$. Check: $\sqrt4=2$ yes; $\sqrt1=1\neq-1$ no. Solution set $\{2\}$.

## Variant 08 (of ANA UE01/8)
$n=1$: $1\cdot2=2=\frac{1\cdot2\cdot3}{3}$. Step: $\sum_{i=1}^{n+1}i(i+1)=\frac{n(n+1)(n+2)}{3}+(n+1)(n+2)
=\frac{(n+1)(n+2)(n+3)}{3}$, factoring out $(n+1)(n+2)$, which the target contains.

## Board
- **UE01/1:** $\mathbb{Z}_2$ has two elements, so every axiom is a finite check. Neutral elements and inverses from the
  table ($-1=1$, $1^{-1}=1$). Associativity: any triple with a $0$ reduces to the sum of the other two; only $1,1,1$ is
  computed. Distributivity: split on $a$.
- **UE01/2:** (a) $\frac{x^2+y^2}{2}-|xy|=\frac{(|x|-|y|)^2}{2}\ge0$. (b) Lemma: for $u,v\ge0$, $u\le v\Leftrightarrow
  u^2\le v^2$; apply it to $|x|,|y|$. Picture: the double wedge around the $y$-axis.
- **UE01/3:** sketch the three sets (turn $\le$ into $=$, quadrant by quadrant). Prove $A_1\subseteq A_2$ by $t^2\le t$ on
  $[0,1]$, $A_2\subseteq A_\infty$ by $x^2\le1\Rightarrow|x|\le1$. Witnesses $(\frac1{\sqrt2},\frac1{\sqrt2})$, $(1,1)$.
- **UE01/4:** (a) arbitrary $x$, chain of $\Leftrightarrow$, $\cup$ becomes $\vee$, "x arbitrary". (b) the eight answers,
  each with its one-line reason; show the parabola with the band.
- **UE01/5:** solve $f(a)=b$ for each map. $f_1$: $-1$ has no preimage, $|{-1}|=|1|$. $f_2$: two branches, opposite
  signs, $f_2\circ f_2=\mathrm{id}$. $f_3$: injective via $a^2=b^2$, $a,b\ge0$; image $(0,1]$.
- **UE01/6:** (a) wlog $x_1<x_2$, then $f(x_1)\neq f(x_2)$. (b) bijective, then: $y_1<y_2$, suppose $x_1\ge x_2$,
  monotonicity gives $y_1\ge y_2$. Name monotonicity, not injectivity.
- **UE01/7:** $A\Rightarrow B$ by substitution; $B\Rightarrow A$ fails at $(5,0)$; $L_1=\{(5,-4)\}$ after plugging in;
  $L_2=\emptyset$. Mention the asymptote parallel to the line.
- **UE01/8:** base case, then split off $(n+1)^3$, use the hypothesis, factor $(n+1)^2$, get $(n+2)^2$.
