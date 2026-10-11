% Kaelearn: the Night Console folio. One committed look: phosphor on charcoal,
% LED-dot frames, dither only in scenery. See system/design.md.
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{kaelearn}[2026/10/11 Kaelearn Night Console]
\LoadClass[11pt,oneside]{article}
\providecommand\KLROOT{./}% engine/ with a trailing slash; kl.py passes it

% iPad-native page (4:3); the outer column holds his asides and your ink.
\RequirePackage[paperwidth=210mm,paperheight=280mm,left=19mm,right=60mm,top=27mm,bottom=25mm,
  marginparwidth=40mm,marginparsep=7mm,headheight=14pt,headsep=9mm,footskip=13mm]{geometry}
\RequirePackage{xcolor}
\RequirePackage{amsmath,amsthm}
\RequirePackage{fontspec}
\RequirePackage{unicode-math}
\RequirePackage{etoolbox,needspace,graphicx,tikz,pgfplots,enumitem,fancyhdr,titlesec,tabularx,array,lastpage,refcount}
\RequirePackage[most]{tcolorbox}
\usetikzlibrary{patterns.meta,decorations.pathmorphing,calc,arrows.meta,positioning}
\usepgfplotslibrary{fillbetween}
\pgfplotsset{compat=1.18}
\graphicspath{{./}{figs/}{\KLROOT art/}}

% ---- palette: the console's inks ---------------------------------------------
\definecolor{klpage}{HTML}{121212}  % ground, never pure black
\definecolor{klink}{HTML}{C5BCAB}   % phosphor: body text
\definecolor{klhi}{HTML}{E6E0D4}    % headings, emphasis
\definecolor{kldim}{HTML}{8A8376}   % labels, captions, asides
\definecolor{kllow}{HTML}{4C4741}   % LED dots, rules
\definecolor{klfaint}{HTML}{1B1A18} % quiet fills
\definecolor{klseal}{HTML}{8E2B22}  % wax only, nothing else is red
\definecolor{klsealdk}{HTML}{5E1A14}
\definecolor{klsealhi}{HTML}{B8483B}
\pagecolor{klpage}\color{klink}

% ---- type --------------------------------------------------------------------
\defaultfontfeatures{Ligatures=TeX}
\setmainfont{EBGaramond}[Path=\KLROOT fonts/,Extension=.otf,UprightFont=*-Medium,ItalicFont=*-MediumItalic,
  BoldFont=*-Bold,BoldItalicFont=*-BoldItalic]
\setmathfont{Garamond-Math.otf}[Path=\KLROOT fonts/,StylisticSet={7,9}]
\newfontfamily\goth{UnifrakturMaguntia-Book.ttf}[Path=\KLROOT fonts/]
\newfontfamily\fell{IMFellEnglish.ttf}[Path=\KLROOT fonts/,ItalicFont=IMFellEnglish-Italic.ttf]
\newfontfamily\pixf{Silkscreen.ttf}[Path=\KLROOT fonts/]
\newfontfamily\tek{Tektur.ttf}[Path=\KLROOT fonts/]
\newfontfamily\mono{GeistMono-Regular.otf}[Path=\KLROOT fonts/,Scale=MatchLowercase]
\linespread{1.08}
\setlength{\parindent}{1.1em}
\frenchspacing
\emergencystretch=1.5em% a looser line beats one that runs into the margin

\newcommand\pix[1]{{\leavevmode\pixf\fontsize{6.8}{8.5}\selectfont\addfontfeature{LetterSpace=3.5}\MakeUppercase{#1}}}
\newcommand\de[1]{{\leavevmode\fell\itshape\color{kldim}#1}}% a German term
\newcommand\twodigit[1]{\ifnum#1<10 0\fi#1}
\tikzset{leds/.style={line width=1.15pt,line cap=round,dash pattern=on 0pt off 2.9pt}}
\newcommand\ledline[1]{\tikz[baseline=-.5ex]\draw[kllow,leds](0,0)--(#1,0);}

% ---- metadata ----------------------------------------------------------------
\newcommand\subject[1]{\def\kl@subject{#1}}
\newcommand\folio[1]{\def\kl@folio{#1}}
\newcommand\shorttitle[1]{\def\kl@short{#1}}
\newcommand\subtitle[1]{\def\kl@subtitle{#1}}
\newcommand\sources[1]{\def\kl@sources{#1}}
\newcommand\readtime[1]{\def\kl@read{#1}}
\newcommand\filed[1]{\def\kl@filed{#1}}
\newcommand\plate[2]{\def\kl@plate{#1}\def\kl@platename{#2}}
\newcommand\kael[1]{\def\kl@kael{#1}}
\subject{}\folio{00}\shorttitle{}\subtitle{}\sources{}\readtime{}\filed{\today}\kael{reading}

% ---- running head, LED page meter --------------------------------------------
\newcommand\kl@leds{%
  \edef\kl@n{\getpagerefnumber{LastPage}}%
  \ifnum\kl@n>0 \ifnum\kl@n<40
    \begin{tikzpicture}[baseline=-.6ex]
      \foreach \i in {1,...,\kl@n}{%
        \ifnum\i>\value{page}\fill[kllow](\i*7pt,0) circle (1.9pt);\else\fill[klink](\i*7pt,0) circle (1.9pt);\fi}
    \end{tikzpicture}%
  \fi\fi}
\pagestyle{fancy}\fancyhf{}
\fancyheadoffset[R]{47mm}\fancyfootoffset[R]{47mm}
\renewcommand\headrule{\vskip3pt\ledline{\headwidth}}
\fancyhead[L]{\color{kldim}\pix{Kaelearn // \kl@subject\ // \kl@folio}}
\fancyhead[R]{\color{kldim}\pix{\kl@short}}
\fancyfoot[L]{\kl@leds}
\fancyfoot[R]{{\tek\fontsize{10}{10}\selectfont\color{kldim}\twodigit{\thepage}}}

% ---- headings ----------------------------------------------------------------
% sections are "Part I"; a sheet that goes problem by problem (debriefs) says \problemparts
\newcommand\kl@part{Part \Roman{section}}
\newcommand\problemparts{\renewcommand\kl@part{Problem \twodigit{\arabic{section}}}}
\titleformat{\section}[display]{\color{klhi}}{\color{kldim}\pix{\kl@part}}{1pt}{\goth\fontsize{25}{28}\selectfont}
\titlespacing*{\section}{0pt}{16pt}{9pt}
\titleformat{\subsection}{\fell\fontsize{14}{16}\selectfont\color{klhi}}{}{0pt}{}
\titlespacing*{\subsection}{0pt}{11pt}{4pt}
\newcommand\opening[2]{\textsc{#1#2}}% first words of a part, in small caps

% ---- Kael'thos in the margin ---------------------------------------------------
\newcommand\aside[1]{\marginpar{\raggedright\fell\itshape\fontsize{10.5}{12.8}\selectfont\color{kldim}#1}}
\newcommand\marginkael[1]{\marginpar{\centering\includegraphics[width=30mm]{#1}}}

% ---- frames: dotted LED border, pixel title strip, a square at the right ----
\newcommand\kl@title[3]{\pix{#1\ifstrempty{#2}{}{ // #2}\ifstrempty{#3}{}{ · #3}}}
\tcbset{klframe/.style={enhanced,breakable,colback=klpage,colupper=klink,coltitle=kldim,colbacktitle=klpage,
  boxrule=0pt,arc=0pt,frame hidden,left=10pt,right=10pt,top=7pt,bottom=8pt,toptitle=4pt,bottomtitle=4pt,
  before skip=11pt,after skip=11pt,titlerule=0pt,fonttitle=\normalfont,
  frame code={\draw[kllow,leds]([shift={(.6pt,.6pt)}]frame.south west) rectangle ([shift={(-.6pt,-.6pt)}]frame.north east);},
  overlay unbroken and first={\draw[kllow,leds]([xshift=.6pt]title.south west)--([xshift=-.6pt]title.south east);
    \fill[kldim]([xshift=-9pt]title.east) ++(-2.6pt,-2.6pt) rectangle ++(5.2pt,5.2pt);}}}
% [tcolorbox options], #2 kind, #3 name, #4 German name; either name may be empty.
% [unbreakable] keeps a short panel in one piece.
\newtcolorbox{panel}[4][]{klframe,title={\kl@title{#2}{#3}{#4}},#1}
\newtcolorbox{twominute}{klframe,title={\kl@title{The two-minute view}{read this first}{}}}
\newtcolorbox{guessfirst}{klframe,title={\kl@title{Guess first}{wrong is fine, guessing is the point}{}}}
\newcounter{klitem}
\newenvironment{definition}[2]{\refstepcounter{klitem}\begin{panel}{Definition \kl@folio.\theklitem}{#1}{#2}}{\end{panel}}
\newenvironment{theorem}[2]{\refstepcounter{klitem}\begin{panel}{Theorem \kl@folio.\theklitem}{#1}{#2}}{\end{panel}}
\newenvironment{example}[1]{\refstepcounter{klitem}\begin{panel}{Example \kl@folio.\theklitem}{#1}{}}{\end{panel}}
% the keystone: the one theorem the folio exists for, sealed in wax (once per folio)
\newenvironment{keystone}[2]{\refstepcounter{klitem}\begin{tcolorbox}[klframe,title={\kl@title{Theorem \kl@folio.\theklitem}{#1}{#2}},
  overlay unbroken and first app={\node at ([xshift=-22pt,yshift=-14pt]frame.north east){\waxseal};}]}{\end{tcolorbox}}
\renewcommand\qedsymbol{\textcolor{kldim}{\rule{1.1ex}{1.1ex}}}
\renewcommand\proofname{\textsc{Proof}}

% Why: the question in the open, the word in the margin
\newcommand\why[2]{\par\medskip\needspace{5\baselineskip}\noindent\marginpar{\vspace{-3pt}\goth\fontsize{19}{19}\selectfont\color{klhi}Why?}%
  {\fell\itshape\fontsize{12.5}{15}\selectfont\color{klhi}#1}\par\smallskip\noindent\hangindent=1.1em\hangafter=0 #2\par\medskip}

\setlist{nosep,leftmargin=1.2em}
\setlist[itemize]{label={\color{kldim}\raisebox{.2ex}{\tikz\fill (0,0) circle (1.25pt);}}}
\setlist[enumerate]{label={\color{kldim}\tek\fontsize{8.5}{10}\selectfont 0\arabic*}}

% ---- tables: terms, triggers, cards -----------------------------------------
\newcommand\kl@rule[1]{\noalign{\vskip2pt}\multicolumn{#1}{@{}l@{}}{\ledline{\linewidth}}\\\noalign{\vskip1pt}}
\newcommand\term[3]{#1 & \de{#2} & #3\\\kl@rule{3}}
\newenvironment{terms}{\subsection{Terms \de{· Begriffe}}\noindent\begin{tabular}{@{}>{\raggedright}p{33mm}>{\raggedright}p{33mm}%
  >{\raggedright\arraybackslash}p{\dimexpr\linewidth-66mm-4\tabcolsep\relax}@{}}
  {\color{kldim}\pix{English}} & {\color{kldim}\pix{Deutsch}} & {\color{kldim}\pix{In one line}}\\\kl@rule{3}}{\end{tabular}\par}
\newcommand\trigger[2]{#1 & #2\\\kl@rule{2}}
\newenvironment{triggers}{\begin{panel}{Triggers}{if you see this, reach for that}{}\noindent
  \begin{tabular}{@{}>{\raggedright}p{58mm}>{\raggedright\arraybackslash}p{\dimexpr\linewidth-58mm-2\tabcolsep\relax}@{}}
  {\color{kldim}\pix{You see}} & {\color{kldim}\pix{Reach for}}\\\kl@rule{2}}
  {\end{tabular}\end{panel}}
\newtcolorbox{deck}{klframe,title={\kl@title{For the deck}{make these yourself, the making is the learning}{}}}
\newcommand\card[3]{\par\smallskip\noindent\begin{tabularx}{\linewidth}{@{}p{14mm}X@{\hspace{8pt}}X@{}}
  {\color{kldim}\pix{#1}} & #2 & {\color{kldim}#3}\end{tabularx}\par\smallskip}

% ---- sheets: problems and room to write -------------------------------------
\newcounter{klproblem}
\newcommand\problem[1][]{\par\bigskip\noindent\refstepcounter{klproblem}%
  {\tek\fontsize{11}{11}\selectfont\color{klhi}\twodigit{\theklproblem}}\hspace{8pt}\ifstrempty{#1}{}{{\color{kldim}\pix{#1}}\hspace{6pt}}}
% an LED-dot grid to write on in Notability: \answerspace{height}
\newcommand\answerspace[1]{\par\smallskip\noindent
  \pgfmathtruncatemacro\kl@w{\linewidth/1mm-1}\pgfmathtruncatemacro\kl@h{(#1)/1mm-1}%
  \begin{tikzpicture}\foreach \x in {0,5,...,\kl@w}{\foreach \y in {0,5,...,\kl@h}{\fill[kllow](\x mm,-\y mm) circle (.55pt);}}
  \end{tikzpicture}\par\smallskip}

% ---- animations: the poster frame; a tap plays the video in Obsidian ----------
% \anim{slug}{what to watch for}: anims/slug.png here, slug.mp4 published beside this PDF
\providecommand\KLVAULT{}
\newcommand\anim[2]{\begin{panel}[unbreakable]{Animation}{#1}{tap to play}
  \noindent\href{\KLVAULT #1.mp4}{\includegraphics[width=\linewidth]{anims/#1.png}}\par\smallskip
  {\fell\itshape\fontsize{10.5}{13}\selectfont\color{kldim}#2}\end{panel}}

% ---- the wax seal (the one red thing) ---------------------------------------
\newcommand\waxseal{\begin{tikzpicture}[scale=.5]
  \fill[klsealdk,decorate,decoration={random steps,segment length=1.4pt,amplitude=.7pt}](0,0) circle (1.02);
  \fill[klseal,decorate,decoration={random steps,segment length=1.1pt,amplitude=.45pt}](0,0) circle (.92);
  \draw[klsealdk,line width=.9pt](0,0) circle (.66);
  \fill[klsealhi,opacity=.55](-.38,.42) circle (.13);
  \node[text=klsealdk] at (0,-.03){\goth\fontsize{15}{15}\selectfont K};
\end{tikzpicture}}

% ---- figures: pgfplots in the console's inks, 1-bit dither fills -------------
\tikzdeclarepattern{name=dither25,type=uncolored,bounding box={(0,0) and (2.4pt,2.4pt)},tile size={(2.4pt,2.4pt)},
  code={\fill (0,0) rectangle (.75pt,.75pt);}}
\tikzdeclarepattern{name=dither50,type=uncolored,bounding box={(0,0) and (2.4pt,2.4pt)},tile size={(2.4pt,2.4pt)},
  code={\fill (0,0) rectangle (.75pt,.75pt);\fill (1.2pt,1.2pt) rectangle (1.95pt,1.95pt);}}
\pgfplotsset{klplot/.style={axis lines=left,axis line style={kldim,line width=.6pt,-},tick style={kldim,line width=.5pt},
  every tick label/.append style={font=\tek\fontsize{7}{8}\selectfont,text=kldim},label style={text=klink},
  every axis plot/.append style={line width=.9pt},cycle list={{klhi},{klink,dashed},{kldim},{klink,dotted}},
  clip=false,width=\linewidth,height=55mm}}
\tikzset{every picture/.append style={color=klink,text=klink}}
\newcommand\plotcaption[1]{\par\smallskip{\fell\itshape\fontsize{10.5}{13}\selectfont\color{kldim}#1}\par\medskip}

% ---- the cover (folios) and the header (sheets) ------------------------------
\newcommand\kl@kv[2]{{\color{kldim}\pix{#1}} & {\mono\fontsize{8.5}{11}\selectfont\color{klink}#2}\\}
\newcommand\makecover{%
  \thispagestyle{empty}%
  \begin{tikzpicture}[remember picture,overlay]
    \coordinate (P) at ([xshift=14mm,yshift=-16mm]current page.north west);
    \node[anchor=north west,inner sep=0] (plate) at ([yshift=-7mm]P){\includegraphics[width=182mm]{\kl@plate}};
    \draw[kllow,leds](P) rectangle ([xshift=.5mm,yshift=-.5mm]plate.south east);
    \draw[kllow,leds]([yshift=-7mm]P)--++(182.5mm,0);
    \node[anchor=west,text=kldim] at ([xshift=4mm,yshift=-3.5mm]P){\pix{Plate // \kl@platename}};
    \fill[kldim]([xshift=178mm,yshift=-3.5mm]P) ++(-2.6pt,-2.6pt) rectangle ++(5.2pt,5.2pt);
    \node[anchor=north west,text=kldim] at ([yshift=-8mm]P |- plate.south){\pix{Kaelearn // \kl@subject\ // Folio \kl@folio}};
    \node[anchor=north west,text=klhi,align=left,inner sep=0,font=\goth\fontsize{50}{50}\selectfont] (t)
      at ([yshift=-15mm]P |- plate.south){\@title};
    \node[anchor=north west,text=klink,align=left,inner sep=0,font=\fell\itshape\fontsize{15}{18}\selectfont] (s)
      at ([yshift=-5mm]t.south west){\kl@subtitle};
    \node[anchor=north west,inner sep=0] at ([yshift=-9mm]s.south west){\begin{tabular}{@{}l@{\hspace{8mm}}l@{}}
      \kl@kv{Folio}{\kl@folio}\kl@kv{Subject}{\kl@subject}\kl@kv{Sources}{\kl@sources}\kl@kv{Read}{\kl@read}\kl@kv{Filed}{\kl@filed}\end{tabular}};
    \node[anchor=south east,inner sep=0] at ([xshift=-12mm,yshift=17mm]current page.south east){\includegraphics[width=58mm]{\kl@kael}};
    \draw[kllow,leds]([xshift=14mm,yshift=17.5mm]current page.south west)--([xshift=-14mm,yshift=17.5mm]current page.south east);
  \end{tikzpicture}%
  \clearpage}
\newcommand\makeheader{%
  \thispagestyle{fancy}%
  \noindent{\color{kldim}\pix{Kaelearn // \kl@subject\ // \kl@folio}}\par\smallskip
  \noindent{\goth\fontsize{34}{36}\selectfont\color{klhi}\@title}\par\smallskip
  \ifdefempty{\kl@subtitle}{}{\noindent{\fell\itshape\fontsize{13}{16}\selectfont\color{klink}\kl@subtitle}\par}
  \medskip\noindent\ledline{\linewidth}\par\medskip}

\RequirePackage[hidelinks,bookmarksopen]{hyperref}
\RequirePackage{xurl}
\def\UrlFont{\mono\fontsize{8}{10}\selectfont\color{kldim}}
\endinput
