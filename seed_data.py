#!/usr/bin/env python
"""
Django Seed Script — UGC NET Paper 1 & Paper 2 (CS & IT)
Run:  python manage.py shell < seed_data.py
  or: python seed_data.py  (from project root)
"""
import os, sys, re

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ugc_net_django.settings')
import django
django.setup()

from core.models import Subject, Topic, Question

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text.strip('-')

PAPER1_SUBJECTS = [

    # ── Unit 1: Teaching Aptitude ───────────────────────
    {
        'name': 'Teaching Aptitude',
        'icon': '🏫', 'color': '#7c3aed',
        'description': 'Nature, objectives, levels, methods, evaluation and characteristics of effective teaching',
        'topics': [
            {
                'title': 'Nature and Objectives of Teaching',
                'summary': 'Teaching is a purposeful, planned, and interactive activity aimed at enabling learning.',
                'difficulty': 'easy', 'estimated_minutes': 25,
                'content': """## What is Teaching?

Teaching is a **complex, purposeful and interactive process** through which the teacher facilitates learning in students. It involves sharing knowledge, developing critical thinking, fostering positive attitudes, and creating an environment conducive to learning.

## Characteristics of Good Teaching

1. **Purposeful** — has clear learning objectives
2. **Interactive** — involves two-way communication
3. **Systematic** — follows a planned structure
4. **Flexible** — adapts to learner needs
5. **Democratic** — respects learner's opinions

## Objectives of Teaching — Bloom's Taxonomy

| Domain | Focus | Example |
|--------|-------|---------|
| **Cognitive** | Knowledge & thinking | Understanding, Applying, Evaluating |
| **Affective** | Attitudes & values | Appreciating, Valuing |
| **Psychomotor** | Physical skills | Drawing, Performing |

## Levels of Teaching

- **Memory Level** (Herbartian) — rote recall of facts
- **Understanding Level** (Morrison) — comprehension and interpretation
- **Reflective Level** (Hunt) — critical thinking, problem-solving, creativity

> **Key Insight:** Modern teaching emphasises moving from memory level to reflective level.

## Teaching vs Training vs Instruction

| Term | Scope |
|------|-------|
| Teaching | Broad — cognitive, affective, psychomotor |
| Training | Narrow — skill-focused |
| Instruction | Procedural — giving directions |
""",
            },
            {
                'title': 'Methods and Approaches of Teaching',
                'summary': 'Different teaching methods suit different content types and learner needs.',
                'difficulty': 'medium', 'estimated_minutes': 35,
                'content': """## Major Teaching Methods

### 1. Lecture Method
Traditional teacher-centred delivery.
- **Advantages:** Covers large content quickly
- **Disadvantages:** Passive, low engagement

### 2. Discussion Method
Structured dialogue between teacher and students.
- **Types:** Whole class, Small group, Panel discussion

### 3. Demonstration Method
Teacher shows how to perform a task — best for Science, Vocational, PE.

### 4. Problem-Solving Method
Steps: Identify → Collect data → Form hypothesis → Test → Conclude

### 5. Project Method
Real-world projects. Developed by **William Kilpatrick** based on **John Dewey's** philosophy of *learning by doing*.

### 6. Inquiry/Discovery Method
Students discover knowledge through investigation and experimentation.

### 7. Cooperative Learning
Heterogeneous small groups working toward shared goals.

## Approaches to Teaching

| Approach | Focus |
|----------|-------|
| Teacher-centred | Teacher is information source |
| Learner-centred | Student needs prioritised |
| Content-centred | Curriculum focus |
| Activity-centred | Learning through doing |

> **Current Trend:** UGC NET emphasises **constructivist** and **learner-centred** approaches.
""",
            },
            {
                'title': 'Characteristics of Learners and Evaluation',
                'summary': 'Understanding learner characteristics and designing appropriate evaluation systems.',
                'difficulty': 'medium', 'estimated_minutes': 30,
                'content': """## Learner Characteristics

Effective teaching requires understanding:
- **Age and developmental stage** — Piaget's cognitive stages
- **Prior knowledge and experience**
- **Learning styles** — Visual, Auditory, Kinesthetic (VAK model)
- **Motivation** — Intrinsic vs Extrinsic
- **Socio-economic background**

## Piaget's Cognitive Development Stages

| Stage | Age | Characteristics |
|-------|-----|-----------------|
| Sensorimotor | 0–2 | Object permanence |
| Preoperational | 2–7 | Symbolic thinking |
| Concrete Operational | 7–11 | Logical operations |
| Formal Operational | 12+ | Abstract reasoning |

## Evaluation in Teaching

### Types of Evaluation
- **Formative** — ongoing, during instruction (quizzes, assignments)
- **Summative** — end of course (final exams, term papers)
- **Diagnostic** — identifies learning difficulties before instruction
- **Norm-Referenced** — compares student with peers
- **Criterion-Referenced** — compares student against a standard

### Characteristics of Good Evaluation
1. **Validity** — measures what it intends to
2. **Reliability** — consistent results
3. **Objectivity** — free from personal bias
4. **Practicability** — feasible to administer
5. **Comprehensiveness** — covers all objectives

## Continuous and Comprehensive Evaluation (CCE)
Introduced to reduce exam stress and assess all-round development including:
- Scholastic areas (subjects)
- Co-scholastic areas (sports, arts, values)
""",
            },
        ],
        'questions': [
            {
                'question_text': 'Which level of teaching is associated with critical thinking and reflective thought?',
                'option_a': 'Memory Level', 'option_b': 'Understanding Level',
                'option_c': 'Reflective Level', 'option_d': 'Application Level',
                'correct_answer': 'C', 'difficulty': 'medium',
                'explanation': 'Reflective Level (Hunt) involves critical thinking, problem-solving and creativity — the highest level of teaching.'
            },
            {
                'question_text': 'The Project Method of teaching was developed by:',
                'option_a': 'John Dewey', 'option_b': 'William Kilpatrick',
                'option_c': 'Jean Piaget', 'option_d': 'Herbart',
                'correct_answer': 'B', 'difficulty': 'easy',
                'explanation': 'The Project Method was developed by William Kilpatrick, based on John Dewey\'s philosophy of learning by doing.'
            },
            {
                'question_text': 'Bloom\'s Taxonomy classifies educational objectives into how many domains?',
                'option_a': '2', 'option_b': '4', 'option_c': '3', 'option_d': '5',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'Bloom\'s Taxonomy classifies objectives into three domains: Cognitive, Affective and Psychomotor.'
            },
            {
                'question_text': 'Which type of evaluation is conducted at the end of a course to measure overall achievement?',
                'option_a': 'Formative', 'option_b': 'Diagnostic',
                'option_c': 'Summative', 'option_d': 'Criterion-referenced',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'Summative evaluation is conducted at the end of an instructional unit to assess total learning.'
            },
            {
                'question_text': 'According to Piaget, at which stage does abstract reasoning develop?',
                'option_a': 'Sensorimotor', 'option_b': 'Preoperational',
                'option_c': 'Concrete Operational', 'option_d': 'Formal Operational',
                'correct_answer': 'D', 'difficulty': 'medium',
                'explanation': 'Abstract reasoning develops during the Formal Operational stage (12+ years) in Piaget\'s cognitive development model.'
            },
        ]
    },

    # ── Unit 2: Research Aptitude ────────────────────────
    {
        'name': 'Research Aptitude',
        'icon': '🔬', 'color': '#0891b2',
        'description': 'Research methods, types, ethics, steps and evaluation in academic research',
        'topics': [
            {
                'title': 'Research: Meaning, Types and Characteristics',
                'summary': 'Research is a systematic and scientific inquiry to find solutions to problems or add to existing knowledge.',
                'difficulty': 'easy', 'estimated_minutes': 30,
                'content': """## Meaning of Research

Research is a **careful, systematic, patient study and investigation** in some field of knowledge, undertaken to establish facts and principles. Derived from French *recherche* meaning "to search again."

## Characteristics of Good Research

- **Systematic** — follows a planned procedure
- **Logical** — applies logical reasoning
- **Empirical** — based on observable, verifiable evidence
- **Replicable** — can be repeated to verify results
- **Objective** — free from personal bias
- **Critical** — examines methods and conclusions critically
- **Ethical** — follows ethical guidelines

## Types of Research

### By Purpose
| Type | Description |
|------|-------------|
| **Fundamental/Basic** | Extends knowledge without immediate application |
| **Applied** | Solves specific practical problems |
| **Action Research** | Improves practices in specific settings (e.g., classroom) |

### By Method
- **Descriptive Research** — describes current status of a phenomenon
- **Historical Research** — studies past events and their significance
- **Experimental Research** — tests cause-effect relationships with controlled variables
- **Survey Research** — collects data from large populations
- **Case Study** — in-depth study of a single unit

### By Nature of Data
| Type | Data Used |
|------|-----------|
| **Quantitative** | Numbers, statistics |
| **Qualitative** | Words, meanings, descriptions |
| **Mixed Methods** | Combines both |
""",
            },
            {
                'title': 'Research Methods and Steps',
                'summary': 'The systematic steps of research process and key research methods used in academia.',
                'difficulty': 'medium', 'estimated_minutes': 35,
                'content': """## Steps in the Research Process

1. **Identification of Research Problem** — select a researchable, significant problem
2. **Review of Literature** — study existing work to avoid duplication
3. **Formulation of Hypothesis** — testable prediction about the relationship between variables
4. **Research Design** — blueprint for data collection and analysis
5. **Data Collection** — gathering information using appropriate tools
6. **Data Analysis and Interpretation** — applying statistical or qualitative methods
7. **Conclusions and Generalizations** — drawing inferences from results
8. **Report Writing** — documenting the research

## Hypothesis

A hypothesis is a **tentative answer** to the research question.

### Types
- **Null Hypothesis (H₀)** — states no relationship exists between variables
- **Alternative Hypothesis (H₁)** — states a relationship exists
- **Directional** — specifies the direction of the relationship
- **Non-directional** — states a relationship exists without specifying direction

## Variables in Research

| Variable | Definition |
|----------|-----------|
| **Independent** | Cause; manipulated by researcher |
| **Dependent** | Effect; measured by researcher |
| **Extraneous/Confounding** | Interferes with the relationship; must be controlled |

## Data Collection Tools

- **Questionnaire** — written set of questions; suitable for large samples
- **Interview** — oral questioning; deeper insights
- **Observation** — systematic watching; naturalistic or structured
- **Rating Scale** — Likert, semantic differential scales
- **Tests** — standardised instruments

## Sampling Methods

### Probability Sampling
- Simple Random Sampling
- Stratified Sampling
- Cluster Sampling
- Systematic Sampling

### Non-Probability Sampling
- Purposive Sampling
- Convenience Sampling
- Snowball Sampling
""",
            },
            {
                'title': 'Research Ethics and Report Writing',
                'summary': 'Ethical responsibilities in research and structure of academic research reports.',
                'difficulty': 'medium', 'estimated_minutes': 25,
                'content': """## Research Ethics

Ethics ensures that research is conducted with **integrity, honesty, and respect** for participants.

### Key Ethical Principles
1. **Informed Consent** — participants must voluntarily agree, knowing the study's purpose
2. **Confidentiality** — participants' identities must be protected
3. **Anonymity** — data not traceable to individuals
4. **Non-maleficence** — avoid harm to participants
5. **Beneficence** — research should benefit society
6. **Plagiarism-free** — original work, properly cited

### Research Misconduct
- **Fabrication** — making up data
- **Falsification** — manipulating data
- **Plagiarism** — presenting others' work as your own

## Academic Writing and Publication

### Types of Academic Writing
- **Research Paper** — original study published in journals
- **Review Article** — synthesises existing research
- **Thesis/Dissertation** — for degrees (Master's/PhD)
- **Conference Paper** — presented at academic conferences

### Citation Styles
- **APA** (American Psychological Association) — social sciences
- **MLA** (Modern Language Association) — humanities
- **Chicago** — history, arts
- **IEEE** — engineering and technology

## Structure of a Research Report

1. Title Page
2. Abstract (150–250 words)
3. Introduction and Background
4. Review of Literature
5. Methodology
6. Results and Discussion
7. Conclusions
8. References/Bibliography
9. Appendices

## Seminar, Workshop, Symposium, Conference

| Format | Purpose |
|--------|---------|
| **Seminar** | Small group, expert-led discussion |
| **Workshop** | Skill-building, hands-on |
| **Symposium** | Multiple experts on one topic |
| **Conference** | Large gathering, paper presentations |
""",
            },
        ],
        'questions': [
            {
                'question_text': 'Which type of research aims to solve an immediate, practical problem?',
                'option_a': 'Fundamental Research', 'option_b': 'Applied Research',
                'option_c': 'Historical Research', 'option_d': 'Descriptive Research',
                'correct_answer': 'B', 'difficulty': 'easy',
                'explanation': 'Applied research is directed toward solving specific, practical problems in real-world settings.'
            },
            {
                'question_text': 'The Null Hypothesis states that:',
                'option_a': 'There is a significant relationship between variables',
                'option_b': 'There is no relationship between the variables',
                'option_c': 'The dependent variable causes the independent variable',
                'option_d': 'The sample is representative of the population',
                'correct_answer': 'B', 'difficulty': 'medium',
                'explanation': 'The Null Hypothesis (H₀) states there is no significant relationship between the variables being studied.'
            },
            {
                'question_text': 'Which sampling method divides the population into subgroups before sampling?',
                'option_a': 'Simple Random', 'option_b': 'Cluster', 'option_c': 'Stratified', 'option_d': 'Snowball',
                'correct_answer': 'C', 'difficulty': 'medium',
                'explanation': 'Stratified sampling divides the population into strata (subgroups) and then randomly samples from each stratum.'
            },
            {
                'question_text': 'Presenting someone else\'s work as your own in research is called:',
                'option_a': 'Fabrication', 'option_b': 'Falsification', 'option_c': 'Plagiarism', 'option_d': 'Bias',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'Plagiarism is the act of using another person\'s ideas, words, or work without proper attribution.'
            },
            {
                'question_text': 'Action Research is primarily conducted to:',
                'option_a': 'Publish in reputed journals', 'option_b': 'Improve specific professional practices',
                'option_c': 'Build theoretical knowledge', 'option_d': 'Test a null hypothesis',
                'correct_answer': 'B', 'difficulty': 'medium',
                'explanation': 'Action Research is conducted by practitioners (e.g., teachers) to improve their own professional practices in a specific setting.'
            },
        ]
    },

    # ── Unit 3: Reading Comprehension ───────────────────
    {
        'name': 'Reading Comprehension',
        'icon': '📖', 'color': '#059669',
        'description': 'Strategies for reading academic passages, inferencing and answering comprehension questions',
        'topics': [
            {
                'title': 'Reading Comprehension Strategies',
                'summary': 'Effective strategies to read, understand and answer questions based on given passages.',
                'difficulty': 'easy', 'estimated_minutes': 30,
                'content': """## What is Reading Comprehension?

Reading comprehension is the ability to **read text, process it, and understand its meaning**. It is a multi-layered process involving decoding words, building vocabulary, and constructing meaning.

## Levels of Reading Comprehension

| Level | Description |
|-------|-------------|
| **Literal** | What the text explicitly says — factual recall |
| **Inferential** | What the text implies — reading between the lines |
| **Critical/Evaluative** | Judging the quality, relevance, or validity of information |
| **Applied** | Using information from text in new contexts |

## Key Comprehension Skills

1. **Identifying the Main Idea** — the central point the author conveys
2. **Finding Supporting Details** — evidence that backs the main idea
3. **Understanding Vocabulary in Context** — meaning of words from surrounding text
4. **Drawing Inferences** — conclusions based on implied information
5. **Recognising Tone and Purpose** — author's attitude and intent
6. **Summarising** — condensing text into key points

## Common Question Types in UGC NET

- **Direct Questions** — answered from specific lines in the passage
- **Inference Questions** — require logical deduction
- **Vocabulary Questions** — meaning of a word/phrase as used
- **Main Idea Questions** — best title or central theme
- **Author's Purpose** — why the author wrote the passage

## Strategies for Answering Comprehension Questions

1. **Skim first** — read the questions before the passage
2. **Read actively** — underline/note key ideas
3. **Locate, read, answer** — find the relevant section, re-read carefully, then answer
4. **Eliminate wrong options** — use process of elimination
5. **Never bring outside knowledge** — base answers only on the passage

## Tips for UGC NET Comprehension

- Read the passage at least twice
- Pay attention to **transition words** (however, therefore, consequently)
- The answer to inference questions is usually **strongly implied**, not wild guessing
- **Negative questions** ("Which is NOT stated...") require checking all options
""",
            },
        ],
        'questions': [
            {
                'question_text': 'Which level of comprehension involves reading between the lines?',
                'option_a': 'Literal', 'option_b': 'Inferential',
                'option_c': 'Applied', 'option_d': 'Evaluative',
                'correct_answer': 'B', 'difficulty': 'easy',
                'explanation': 'Inferential comprehension involves drawing conclusions that are implied but not explicitly stated in the text.'
            },
            {
                'question_text': 'The best strategy when answering a UGC NET reading comprehension question is to:',
                'option_a': 'Use your general knowledge about the topic',
                'option_b': 'Base answers strictly on information given in the passage',
                'option_c': 'Always choose the most detailed option',
                'option_d': 'Pick the first answer that sounds correct',
                'correct_answer': 'B', 'difficulty': 'easy',
                'explanation': 'Comprehension questions must be answered using only the information provided in the passage, not outside knowledge.'
            },
            {
                'question_text': 'Identifying the author\'s attitude towards the subject is called understanding the:',
                'option_a': 'Main Idea', 'option_b': 'Supporting Details',
                'option_c': 'Tone and Purpose', 'option_d': 'Vocabulary in Context',
                'correct_answer': 'C', 'difficulty': 'medium',
                'explanation': 'Tone refers to the author\'s attitude (e.g., critical, optimistic, neutral) and purpose is why the passage was written.'
            },
        ]
    },

    # ── Unit 4: Communication ────────────────────────────
    {
        'name': 'Communication',
        'icon': '💬', 'color': '#d97706',
        'description': 'Meaning, types, characteristics, barriers and mass media in communication',
        'topics': [
            {
                'title': 'Nature and Types of Communication',
                'summary': 'Communication is the process of conveying information, ideas and feelings between individuals.',
                'difficulty': 'easy', 'estimated_minutes': 30,
                'content': """## Meaning of Communication

Communication comes from Latin *communis* meaning "to share." It is the **process of creating and sharing meaning** through the exchange of messages between a sender and receiver.

## The Communication Process

**Sender → Encoding → Message → Channel → Decoding → Receiver → Feedback**

### Key Elements
| Element | Description |
|---------|-------------|
| **Sender** | Originator of the message |
| **Encoding** | Converting ideas into symbols/words |
| **Message** | Content being communicated |
| **Channel** | Medium (spoken, written, visual) |
| **Decoding** | Receiver interprets the message |
| **Feedback** | Receiver's response to the message |
| **Noise** | Any interference that distorts the message |

## Types of Communication

### By Direction
- **Downward** — Superior to subordinate (instructions, policies)
- **Upward** — Subordinate to superior (reports, feedback)
- **Horizontal/Lateral** — Between peers
- **Diagonal/Crosswise** — Between different levels and departments

### By Mode
| Mode | Examples |
|------|---------|
| **Verbal** | Spoken language, face-to-face |
| **Written** | Letters, emails, reports |
| **Non-verbal** | Body language, gestures, facial expressions |
| **Visual** | Charts, diagrams, videos |

### By Context
- **Intrapersonal** — communication with oneself
- **Interpersonal** — between two people
- **Group** — within a group
- **Mass Communication** — to large, heterogeneous audience via media
""",
            },
            {
                'title': 'Effective Communication and Barriers',
                'summary': 'Characteristics of effective communication and how to identify and overcome barriers.',
                'difficulty': 'medium', 'estimated_minutes': 30,
                'content': """## Characteristics of Effective Communication

1. **Clarity** — message is clear and easily understood
2. **Completeness** — all necessary information is included
3. **Conciseness** — free from redundancy
4. **Correctness** — factually accurate, grammatically correct
5. **Courtesy** — respectful, considerate of receiver
6. **Coherence** — logically organised
7. **Feedback** — two-way process with response

## Barriers to Communication

### 1. Physical Barriers
- Noise, distance, poor infrastructure
- Technical issues in electronic communication

### 2. Psychological/Emotional Barriers
- Fear, stress, prejudice
- **Selective Perception** — filtering information based on biases

### 3. Semantic Barriers
- Ambiguity, use of jargon or technical terms
- Language differences

### 4. Organisational Barriers
- Rigid hierarchies, poor information systems
- Information overload

### 5. Cultural Barriers
- Different cultural norms, values, customs
- Different interpretations of non-verbal cues

## Overcoming Communication Barriers

- Use simple, clear language
- Choose appropriate channel
- Seek and provide feedback
- Be an active listener
- Create a supportive communication climate

## Mass Media and Society

### Types of Mass Media
- **Print Media** — newspapers, magazines, books
- **Electronic/Broadcast Media** — radio, television
- **Digital/New Media** — internet, social media, podcasts

### Functions of Mass Media
1. **Informing** — news and current affairs
2. **Educating** — documentaries, educational programmes
3. **Entertaining** — films, music, sports
4. **Persuading** — advertisements, political campaigns
5. **Socialising** — transmitting cultural values and norms

### Impact of Media on Education
- Expands access to information
- Enables distance and online learning
- Can promote critical thinking
- Risk of misinformation and digital divide
""",
            },
        ],
        'questions': [
            {
                'question_text': 'Which element of the communication process converts ideas into symbols or language?',
                'option_a': 'Decoding', 'option_b': 'Feedback', 'option_c': 'Encoding', 'option_d': 'Channel',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'Encoding is the process by which the sender converts ideas, thoughts, and feelings into a message (words, symbols, etc.).'
            },
            {
                'question_text': 'Communication from a manager to their team about company policy is an example of:',
                'option_a': 'Upward communication', 'option_b': 'Horizontal communication',
                'option_c': 'Downward communication', 'option_d': 'Diagonal communication',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'Downward communication flows from superiors to subordinates — such as instructions, policies, and performance feedback.'
            },
            {
                'question_text': 'Filtering information based on one\'s personal biases is called:',
                'option_a': 'Semantic barrier', 'option_b': 'Selective perception',
                'option_c': 'Information overload', 'option_d': 'Channel noise',
                'correct_answer': 'B', 'difficulty': 'medium',
                'explanation': 'Selective perception occurs when people interpret and remember information selectively based on their attitudes and expectations.'
            },
            {
                'question_text': 'Which form of communication involves the largest heterogeneous audience?',
                'option_a': 'Interpersonal', 'option_b': 'Group', 'option_c': 'Intrapersonal', 'option_d': 'Mass',
                'correct_answer': 'D', 'difficulty': 'easy',
                'explanation': 'Mass communication involves transmitting messages to large, diverse, and geographically scattered audiences through mass media.'
            },
        ]
    },

    # ── Unit 5: Mathematical Reasoning ──────────────────
    {
        'name': 'Mathematical Reasoning',
        'icon': '🔢', 'color': '#be185d',
        'description': 'Number series, letter series, codes, sequences and mathematical aptitude',
        'topics': [
            {
                'title': 'Number Series and Sequences',
                'summary': 'Identify patterns in number sequences — arithmetic, geometric, Fibonacci and mixed series.',
                'difficulty': 'medium', 'estimated_minutes': 40,
                'content': """## Number Series

A number series is a sequence of numbers following a specific pattern or rule.

## Types of Series

### 1. Arithmetic Series
Each term differs by a constant (Common Difference — *d*)

**Formula:** aₙ = a + (n−1)d

**Example:** 2, 5, 8, 11, 14 ... (d = 3)

### 2. Geometric Series
Each term is multiplied by a constant (Common Ratio — *r*)

**Formula:** aₙ = a × rⁿ⁻¹

**Example:** 3, 6, 12, 24, 48 ... (r = 2)

### 3. Fibonacci Series
Each term is the sum of the two preceding terms.

**Example:** 1, 1, 2, 3, 5, 8, 13, 21 ...

### 4. Square/Cube Series
- **Squares:** 1, 4, 9, 16, 25, 36 ...
- **Cubes:** 1, 8, 27, 64, 125 ...

### 5. Mixed/Alternating Series
Two interlaced series alternating positions.

**Example:** 2, 3, 4, 6, 8, 12 ... (Two alternating APs)

## Letter Series

Letters follow number patterns when assigned numeric values (A=1, B=2 ... Z=26).

**Example:** B, D, G, K, P ... (gaps: 2, 3, 4, 5 ...)

## Coding-Decoding

### Types of Codes
- **Letter Substitution:** A→D, B→E ... (shift by 3)
- **Number Substitution:** A=1, B=2 ...
- **Reverse Alphabet:** A=26, B=25 ...

## Relationships and Classification

- **Blood Relations:** Identify relationships using family trees
- **Classification:** Odd one out based on common property

## Quick Tricks

| Series Type | Key Observation |
|-------------|-----------------|
| Arithmetic | Difference between consecutive terms is constant |
| Geometric | Ratio between consecutive terms is constant |
| Fibonacci | Each term = sum of previous two |
| Mixed | Two independent series interleaved |
""",
            },
            {
                'title': 'Mathematical Aptitude: Ratios, Percentages and Data',
                'summary': 'Core mathematical concepts tested in UGC NET: percentages, ratio, profit-loss, and time-work.',
                'difficulty': 'medium', 'estimated_minutes': 45,
                'content': """## Ratios and Proportions

**Ratio** = Comparison of two quantities: a : b = a/b

**Proportion:** a : b = c : d → ad = bc (Cross multiplication)

### Compound Ratio
If a:b and c:d are ratios, their compound ratio = ac:bd

## Percentages

**Percentage = (Part / Whole) × 100**

### Key Formulas
- % increase = [(New − Old) / Old] × 100
- % decrease = [(Old − New) / Old] × 100
- If A is x% of B, then B is (100/x)% of A

## Profit and Loss

- **Profit = SP − CP**
- **Loss = CP − SP**
- **Profit% = (Profit / CP) × 100**
- **Discount = Marked Price − Selling Price**

## Time and Work

If A does a job in *n* days, A's one-day work = 1/n

If A and B together work → Combined one-day work = 1/A + 1/B

## Time, Speed and Distance

**Speed = Distance / Time**

- Average Speed = Total Distance / Total Time
- Relative Speed (same direction) = |S₁ − S₂|
- Relative Speed (opposite direction) = S₁ + S₂

## Simple and Compound Interest

- **SI = P × R × T / 100**
- **CI = P(1 + R/100)ⁿ − P**

## Averages

**Average = Sum of observations / Number of observations**

Weighted Average = Σ(wᵢ × xᵢ) / Σwᵢ
""",
            },
        ],
        'questions': [
            {
                'question_text': 'Find the missing number: 2, 6, 12, 20, 30, __',
                'option_a': '40', 'option_b': '42', 'option_c': '44', 'option_d': '36',
                'correct_answer': 'B', 'difficulty': 'medium',
                'explanation': 'Differences: 4, 6, 8, 10, 12 → next term = 30 + 12 = 42. Pattern: n(n+1): 1×2=2, 2×3=6, 3×4=12, 4×5=20, 5×6=30, 6×7=42.'
            },
            {
                'question_text': 'What is the next term in the series: 1, 1, 2, 3, 5, 8, 13, __?',
                'option_a': '18', 'option_b': '20', 'option_c': '21', 'option_d': '24',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'This is the Fibonacci series where each term = sum of previous two: 8 + 13 = 21.'
            },
            {
                'question_text': 'If A can do a work in 10 days and B can do it in 15 days, in how many days can they finish together?',
                'option_a': '4 days', 'option_b': '5 days', 'option_c': '6 days', 'option_d': '8 days',
                'correct_answer': 'C', 'difficulty': 'medium',
                'explanation': 'A\'s rate = 1/10, B\'s rate = 1/15. Together = 1/10 + 1/15 = 3/30 + 2/30 = 5/30 = 1/6. So together they finish in 6 days.'
            },
            {
                'question_text': 'If a price increases from ₹200 to ₹250, what is the percentage increase?',
                'option_a': '20%', 'option_b': '25%', 'option_c': '50%', 'option_d': '10%',
                'correct_answer': 'B', 'difficulty': 'easy',
                'explanation': '% increase = (250−200)/200 × 100 = 50/200 × 100 = 25%.'
            },
        ]
    },

    # ── Unit 6: Logical Reasoning ────────────────────────
    {
        'name': 'Logical Reasoning',
        'icon': '🧠', 'color': '#7e22ce',
        'description': 'Deductive and inductive reasoning, syllogisms, verbal analogies and Indian logic',
        'topics': [
            {
                'title': 'Deductive and Inductive Reasoning',
                'summary': 'Understanding the structure of arguments and distinguishing between deductive and inductive reasoning.',
                'difficulty': 'medium', 'estimated_minutes': 35,
                'content': """## What is an Argument?

An **argument** is a set of statements where one statement (the **conclusion**) is supported by others (the **premises**).

**Structure:** Premise 1 + Premise 2 → Conclusion

## Deductive Reasoning

**Definition:** If premises are true, the conclusion **must necessarily** be true.

**Direction:** General → Specific

**Example:**
- All men are mortal. (Premise 1)
- Socrates is a man. (Premise 2)
- Therefore, Socrates is mortal. (Conclusion) ✅

### Properties
- **Valid** — logical structure is correct (conclusion follows from premises)
- **Sound** — valid AND premises are true
- Invalid deductive arguments can have true premises but false conclusions

## Inductive Reasoning

**Definition:** Conclusion is **probable** based on specific observations.

**Direction:** Specific → General

**Example:**
- The sun rose yesterday, and the day before, and the day before that...
- Therefore, the sun will rise tomorrow. (probable, not certain)

### Strength of Inductive Arguments
- More observations → stronger argument
- Never 100% certain

## Comparing Deductive vs Inductive

| Feature | Deductive | Inductive |
|---------|-----------|----------|
| Direction | General → Specific | Specific → General |
| Certainty | Certain if valid | Probable |
| Conclusion | Necessarily true | Possibly true |
| Invalidation | All-or-nothing | Degree of strength |
""",
            },
            {
                'title': 'Syllogisms and Verbal Analogies',
                'summary': 'Solving syllogism problems using Venn diagrams and identifying analogical relationships.',
                'difficulty': 'hard', 'estimated_minutes': 40,
                'content': """## Syllogisms

A **syllogism** is a three-statement deductive argument: two premises and one conclusion.

### Types of Categorical Propositions

| Type | Form | Example |
|------|------|---------|
| **Universal Affirmative (A)** | All S is P | All cats are animals |
| **Universal Negative (E)** | No S is P | No cats are dogs |
| **Particular Affirmative (I)** | Some S is P | Some cats are white |
| **Particular Negative (O)** | Some S is not P | Some cats are not white |

### Venn Diagram Method
1. Draw circles for each term
2. Shade universal statements
3. Mark particular statements with ×
4. Check if conclusion is always true

### Common Valid Syllogisms
- A + A → A (All A is B, All B is C → All A is C)
- A + E → E (All A is B, No B is C → No A is C)
- I + A → I (Some A is B, All B is C → Some A is C)

## Verbal Analogies

Analogies test relationships between pairs of words.

**Format:** A : B :: C : D ("A is to B as C is to D")

### Common Relationship Types
- **Part to Whole:** Chapter : Book :: Finger : Hand
- **Cause to Effect:** Fire : Burn :: Knife : Cut
- **Tool to User:** Stethoscope : Doctor :: Gavel : Judge
- **Word to Antonym:** Hot : Cold :: Fast : Slow
- **Word to Synonym:** Brave : Courageous :: Quick : Fast
- **Degree of Intensity:** Warm : Hot :: Damp : Wet

## Indian Logic — Nyaya System

The **Nyaya School** (Gautama) is the major system of Indian logic.

### Five-membered Syllogism (Pancavayava)
1. **Pratijna** (Proposition) — The hill has fire
2. **Hetu** (Reason) — Because there is smoke
3. **Udaharana** (Example) — Wherever there is smoke, there is fire, like a kitchen
4. **Upanaya** (Application) — The hill has smoke
5. **Nigamana** (Conclusion) — Therefore, the hill has fire

### Pramana (Sources of Knowledge)
- **Pratyaksha** — Perception (direct knowledge through senses)
- **Anumana** — Inference (knowledge through reasoning)
- **Upamana** — Comparison (knowledge through analogy)
- **Shabda** — Testimony (knowledge through verbal/written authority)
""",
            },
        ],
        'questions': [
            {
                'question_text': 'In a deductive argument, if the premises are true and the argument is valid, the conclusion is:',
                'option_a': 'Probably true', 'option_b': 'Necessarily true',
                'option_c': 'Possibly false', 'option_d': 'Uncertain',
                'correct_answer': 'B', 'difficulty': 'easy',
                'explanation': 'In a valid deductive argument with true premises, the conclusion must necessarily be true.'
            },
            {
                'question_text': '"Stethoscope is to Doctor as Gavel is to __"',
                'option_a': 'Law', 'option_b': 'Court', 'option_c': 'Judge', 'option_d': 'Lawyer',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'This is a Tool : User analogy. A stethoscope is used by a Doctor; a Gavel is used by a Judge.'
            },
            {
                'question_text': 'In Indian logic (Nyaya), direct knowledge through the senses is called:',
                'option_a': 'Anumana', 'option_b': 'Upamana', 'option_c': 'Shabda', 'option_d': 'Pratyaksha',
                'correct_answer': 'D', 'difficulty': 'medium',
                'explanation': 'Pratyaksha (perception) is direct knowledge acquired through the five senses in the Nyaya school of Indian logic.'
            },
            {
                'question_text': 'A Universal Affirmative proposition (A-type) takes the form:',
                'option_a': 'No S is P', 'option_b': 'Some S is P', 'option_c': 'All S is P', 'option_d': 'Some S is not P',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'The A-type proposition is Universal Affirmative: "All S is P", e.g., "All cats are animals."'
            },
        ]
    },

    # ── Unit 7: Data Interpretation ─────────────────────
    {
        'name': 'Data Interpretation',
        'icon': '📊', 'color': '#0f766e',
        'description': 'Reading and interpreting tables, bar charts, pie charts, line graphs and data sets',
        'topics': [
            {
                'title': 'Data Interpretation: Tables and Graphs',
                'summary': 'How to read and extract information from data presented in tabular and graphical forms.',
                'difficulty': 'medium', 'estimated_minutes': 40,
                'content': """## What is Data Interpretation?

Data Interpretation involves **reading, analysing, and drawing conclusions** from data presented in various formats.

## Types of Data

| Type | Description | Example |
|------|-------------|---------|
| **Qualitative** | Categories, labels | Gender, City, Brand |
| **Quantitative (Discrete)** | Countable numbers | Number of students |
| **Quantitative (Continuous)** | Measurable range | Temperature, Weight |

## Data Presentation Formats

### 1. Tables
Organised rows and columns — best for exact values.

**Reading a Table:**
- Read the title and column/row headers first
- Note units of measurement
- Calculate ratios, percentages as required

### 2. Bar Charts
Rectangular bars represent quantities — good for comparison across categories.

- **Simple Bar Chart** — one variable
- **Grouped/Clustered** — multiple variables side by side
- **Stacked Bar Chart** — variables stacked within each bar

### 3. Pie Charts
Circle divided into sectors — shows percentage distribution of a whole.

**Reading:** Angle of sector = (Value / Total) × 360°
If a sector = 72°, it represents 72/360 = 20% of total.

### 4. Line Graphs
Points connected by lines — best for showing **trends over time**.

### 5. Histogram
Frequency distribution — similar to bar chart but for continuous data with no gaps between bars.

### 6. Frequency Polygon
Line graph connecting midpoints of histogram bars — shows distribution shape.

## Key Statistical Measures

| Measure | Formula |
|---------|---------|
| **Mean** | Sum of values / Count |
| **Median** | Middle value when sorted |
| **Mode** | Most frequently occurring value |
| **Range** | Maximum − Minimum |

## Approach to Data Interpretation Questions

1. **Read the question first** — know what to look for
2. **Identify the data format** — table, chart, graph
3. **Note headings, units, scale**
4. **Calculate only what is needed**
5. **Estimate when exact calculation is difficult**
6. **Check for trends** — increasing, decreasing, fluctuating
""",
            },
        ],
        'questions': [
            {
                'question_text': 'If a sector of a pie chart represents 90°, what percentage of the total does it represent?',
                'option_a': '20%', 'option_b': '25%', 'option_c': '30%', 'option_d': '45%',
                'correct_answer': 'B', 'difficulty': 'easy',
                'explanation': 'Percentage = (Angle / 360) × 100 = (90/360) × 100 = 25%.'
            },
            {
                'question_text': 'Which graph is most appropriate for showing changes over time?',
                'option_a': 'Pie Chart', 'option_b': 'Histogram', 'option_c': 'Line Graph', 'option_d': 'Bar Chart',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'Line graphs are best for showing trends and changes over time as they visually connect data points across time periods.'
            },
            {
                'question_text': 'The middle value in a sorted dataset is called the:',
                'option_a': 'Mean', 'option_b': 'Mode', 'option_c': 'Range', 'option_d': 'Median',
                'correct_answer': 'D', 'difficulty': 'easy',
                'explanation': 'The median is the middle value when data is arranged in ascending or descending order.'
            },
        ]
    },

    # ── Unit 8: ICT ──────────────────────────────────────
    {
        'name': 'ICT (Information & Communication Technology)',
        'icon': '💻', 'color': '#1d4ed8',
        'description': 'Basics of computers, internet, e-communication, and ICT tools in education',
        'topics': [
            {
                'title': 'Basics of ICT and Computers',
                'summary': 'Fundamental concepts of ICT, computer hardware, software, and general terminology.',
                'difficulty': 'easy', 'estimated_minutes': 30,
                'content': """## What is ICT?

**Information and Communication Technology (ICT)** encompasses all technologies used to handle information and aid communication, including hardware, software, networks, and the internet.

## Components of a Computer System

### Hardware
| Component | Function |
|-----------|----------|
| **CPU (Central Processing Unit)** | Brain of the computer — processes instructions |
| **RAM** | Temporary working memory |
| **ROM** | Permanent memory; stores boot instructions |
| **Hard Disk (HDD/SSD)** | Permanent storage |
| **Input Devices** | Keyboard, mouse, scanner, microphone |
| **Output Devices** | Monitor, printer, speakers |

### Software
- **System Software** — OS (Windows, Linux, macOS), drivers
- **Application Software** — MS Office, browsers, media players
- **Utility Software** — Antivirus, file management tools

## Number Systems

| System | Base | Digits |
|--------|------|--------|
| Binary | 2 | 0, 1 |
| Octal | 8 | 0–7 |
| Decimal | 10 | 0–9 |
| Hexadecimal | 16 | 0–9, A–F |

**1 Byte = 8 bits**  
**1 KB = 1024 Bytes | 1 MB = 1024 KB | 1 GB = 1024 MB**

## Common Abbreviations

| Abbreviation | Full Form |
|-------------|-----------|
| CPU | Central Processing Unit |
| RAM | Random Access Memory |
| ROM | Read Only Memory |
| OS | Operating System |
| GUI | Graphical User Interface |
| PDF | Portable Document Format |
| HTML | HyperText Markup Language |
| URL | Uniform Resource Locator |
| HTTP | HyperText Transfer Protocol |
| HTTPS | HTTP Secure |
| ISP | Internet Service Provider |
| LAN | Local Area Network |
| WAN | Wide Area Network |
| Wi-Fi | Wireless Fidelity |
""",
            },
            {
                'title': 'Internet, E-mail and ICT in Education',
                'summary': 'Internet basics, e-communication tools, and how ICT transforms teaching and learning.',
                'difficulty': 'easy', 'estimated_minutes': 25,
                'content': """## The Internet

The internet is a **global network of interconnected computers** that communicate using standardised protocols (TCP/IP).

### Key Internet Concepts
- **World Wide Web (WWW)** — a system of interlinked hypertext documents accessed via browsers
- **Browser** — software to navigate the web (Chrome, Firefox, Safari)
- **Search Engine** — Google, Bing, DuckDuckGo
- **Website vs Webpage** — Website is a collection of webpages; a webpage is a single document
- **URL Structure:** `https://www.example.com/page`

### Types of Networks
| Type | Range | Example |
|------|-------|---------|
| **LAN** | Building/campus | Office network |
| **MAN** | City | Cable TV network |
| **WAN** | Country/globe | Internet |

## E-mail

**Electronic Mail (Email)** allows sending and receiving messages over the internet.

### Email Components
- **To** — recipient's address
- **CC** (Carbon Copy) — visible to all recipients
- **BCC** (Blind Carbon Copy) — hidden from other recipients
- **Subject** — brief description of the message
- **Attachment** — files sent along with the email

### Email Safety
- Beware of **phishing** — fraudulent emails mimicking trusted sources
- Never open attachments from unknown senders

## ICT in Education

### Advantages
- Access to vast information resources
- Enables **e-learning** and distance education
- Interactive multimedia learning
- Facilitates collaboration

### ICT Tools for Teaching
- **Learning Management Systems (LMS):** Moodle, Google Classroom
- **MOOCs:** Massive Open Online Courses (Coursera, edX, SWAYAM)
- **Smart Boards** — interactive whiteboards
- **Podcasts and Webcasts** — audio/video educational content

### Disadvantages
- **Digital divide** — unequal access to technology
- Distraction risk
- Cyber security threats
- Over-dependence on technology
""",
            },
        ],
        'questions': [
            {
                'question_text': 'Which memory type is temporary and loses its data when power is switched off?',
                'option_a': 'ROM', 'option_b': 'Hard Disk', 'option_c': 'RAM', 'option_d': 'SSD',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'RAM (Random Access Memory) is volatile — it loses its data when the computer is powered off.'
            },
            {
                'question_text': 'What does "BCC" stand for in email communication?',
                'option_a': 'Basic Carbon Copy', 'option_b': 'Blind Carbon Copy',
                'option_c': 'Background CC', 'option_d': 'Broadcast Carbon Copy',
                'correct_answer': 'B', 'difficulty': 'easy',
                'explanation': 'BCC stands for Blind Carbon Copy — recipients listed here receive the email but their addresses are hidden from other recipients.'
            },
            {
                'question_text': 'SWAYAM is an example of:',
                'option_a': 'A search engine', 'option_b': 'A programming language',
                'option_c': 'A MOOC platform', 'option_d': 'An antivirus software',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'SWAYAM is India\'s national MOOC (Massive Open Online Course) platform offering free courses from school to post-graduate level.'
            },
            {
                'question_text': '1 Gigabyte (GB) is equal to:',
                'option_a': '1000 MB', 'option_b': '1024 MB', 'option_c': '512 MB', 'option_d': '2048 KB',
                'correct_answer': 'B', 'difficulty': 'easy',
                'explanation': '1 GB = 1024 MB in binary (computer) measurement (though 1000 MB = 1 GB in SI units, binary is standard in CS).'
            },
        ]
    },

    # ── Unit 9: People, Development & Environment ────────
    {
        'name': 'People, Development & Environment',
        'icon': '🌍', 'color': '#16a34a',
        'description': 'Human-environment interaction, environmental issues, natural resources and disaster management',
        'topics': [
            {
                'title': 'Development, Environment and Human Interaction',
                'summary': 'How development activities impact the environment and the principles of sustainable development.',
                'difficulty': 'medium', 'estimated_minutes': 35,
                'content': """## Development and Environment

**Development** refers to improving the quality of human life — economic growth, technological advancement, healthcare, and education. However, development often comes with **environmental costs**.

## Human-Environment Interaction

Humans interact with the environment through:
1. **Utilisation** — using natural resources (mining, agriculture, fishing)
2. **Modification** — changing the environment (deforestation, urbanisation, dam construction)
3. **Adaptation** — adjusting human activities to environmental conditions

## Sustainable Development

**Definition (Brundtland Commission, 1987):** "Development that meets the needs of the present without compromising the ability of future generations to meet their own needs."

### Pillars of Sustainable Development
- **Economic** — growth without resource depletion
- **Social** — equity and quality of life
- **Environmental** — conservation and biodiversity

### SDGs (Sustainable Development Goals)
17 goals adopted by the UN in 2015 to achieve sustainable development by 2030.

## Major Environmental Issues

### 1. Climate Change
- **Greenhouse gases** (CO₂, CH₄, N₂O) trap heat in the atmosphere
- **Global Warming** — rising average temperatures
- **Effects:** Sea level rise, extreme weather, glacier melting

### 2. Deforestation
- Loss of forest cover for agriculture, urbanisation, logging
- Consequences: habitat loss, soil erosion, increased CO₂

### 3. Biodiversity Loss
- Species extinction due to habitat destruction, pollution, overexploitation

### 4. Air, Water and Soil Pollution
- **Air Pollution:** Industrial emissions, vehicle exhaust (PM2.5)
- **Water Pollution:** Industrial waste, plastic, agricultural runoff
- **Soil Pollution:** Pesticides, heavy metals, solid waste

## Natural Resources

| Type | Examples |
|------|---------|
| **Renewable** | Solar, Wind, Water, Forests (sustainable use) |
| **Non-renewable** | Coal, Petroleum, Natural Gas, Minerals |

### Conservation Strategies
- **In-situ** — conservation in natural habitat (national parks, wildlife sanctuaries)
- **Ex-situ** — conservation outside habitat (zoos, seed banks, botanical gardens)

## Disaster Management

### Types of Disasters
- **Natural:** Earthquakes, Floods, Tsunamis, Cyclones, Droughts
- **Man-made:** Industrial accidents, Chemical spills, Oil spills

### Phases of Disaster Management
1. **Mitigation** — reducing risk (building codes, early warning systems)
2. **Preparedness** — planning and training
3. **Response** — immediate action during disaster
4. **Recovery** — rebuilding after the disaster

### Key Organisations
- **NDMA** — National Disaster Management Authority (India)
- **NDRF** — National Disaster Response Force
- **UNDRR** — UN Office for Disaster Risk Reduction
""",
            },
        ],
        'questions': [
            {
                'question_text': 'Sustainable Development was defined by which commission in 1987?',
                'option_a': 'United Nations', 'option_b': 'Brundtland Commission',
                'option_c': 'World Bank', 'option_d': 'IPCC',
                'correct_answer': 'B', 'difficulty': 'easy',
                'explanation': 'The Brundtland Commission (World Commission on Environment and Development) defined sustainable development in its 1987 report "Our Common Future."'
            },
            {
                'question_text': 'Conservation of species in their natural habitat is called:',
                'option_a': 'Ex-situ conservation', 'option_b': 'In-situ conservation',
                'option_c': 'Gene banking', 'option_d': 'Captive breeding',
                'correct_answer': 'B', 'difficulty': 'easy',
                'explanation': 'In-situ conservation protects species in their natural habitats — e.g., national parks and wildlife sanctuaries.'
            },
            {
                'question_text': 'Which gas is the primary contributor to the enhanced greenhouse effect?',
                'option_a': 'Oxygen (O₂)', 'option_b': 'Nitrogen (N₂)',
                'option_c': 'Carbon Dioxide (CO₂)', 'option_d': 'Argon (Ar)',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'Carbon dioxide (CO₂) from burning fossil fuels is the primary greenhouse gas responsible for enhanced global warming.'
            },
            {
                'question_text': 'Which phase of disaster management involves immediate relief actions during the disaster?',
                'option_a': 'Mitigation', 'option_b': 'Preparedness', 'option_c': 'Recovery', 'option_d': 'Response',
                'correct_answer': 'D', 'difficulty': 'easy',
                'explanation': 'The Response phase involves all actions taken immediately during or after the disaster — rescue, evacuation, and emergency relief.'
            },
        ]
    },

    # ── Unit 10: Higher Education System ────────────────
    {
        'name': 'Higher Education System',
        'icon': '🎓', 'color': '#92400e',
        'description': 'Evolution, institutions, policies and governance of higher education in India',
        'topics': [
            {
                'title': 'Higher Education in India: History and Evolution',
                'summary': 'Development of higher learning from ancient India to modern times and key institutions.',
                'difficulty': 'medium', 'estimated_minutes': 35,
                'content': """## Higher Education in Ancient India

### Major Centres of Learning
| Institution | Location | Period |
|-------------|----------|--------|
| **Takshashila (Taxila)** | Pakistan | 7th century BCE |
| **Nalanda** | Bihar | 5th–12th century CE |
| **Vikramashila** | Bihar | 8th–12th century CE |
| **Vallabhi** | Gujarat | 5th–8th century CE |

### Gurukul System
- Students lived with the teacher (guru)
- Holistic education — academics, values, physical training
- Oral tradition of knowledge transfer

## Higher Education Post-Independence

### Key Milestones
- **1857** — First three universities established: Calcutta, Bombay, Madras
- **1948** — Radhakrishnan Commission (University Education Commission)
- **1952–53** — Mudaliar Commission (Secondary Education)
- **1964–66** — Kothari Commission (National Education Commission) — recommended 6% GDP on education
- **1986** — National Policy on Education (NPE)
- **1992** — POA (Programme of Action) to implement NPE
- **2020** — **National Education Policy (NEP) 2020** — major reform

## National Education Policy (NEP) 2020

### Key Features
- **5+3+3+4** curricular structure replacing 10+2
- Multidisciplinary approach at university level
- Academic Bank of Credits (ABC)
- Multiple entry and exit options in degree programmes
- Emphasis on Indian languages, arts, vocational education
- Target: **50% Gross Enrolment Ratio (GER)** in higher education by 2035

## Key Regulatory Bodies

| Body | Role |
|------|------|
| **UGC** (University Grants Commission) | Funds and regulates universities |
| **AICTE** (All India Council for Technical Education) | Technical education |
| **MCI** (now NMC — National Medical Commission) | Medical education |
| **BCI** (Bar Council of India) | Legal education |
| **NAAC** | Accredits higher education institutions |
| **NBA** | Accredits technical programmes |
| **NIRF** | National Institutional Ranking Framework |

## Types of Universities in India

- **Central Universities** — established by Parliament (JNU, AMU, BHU)
- **State Universities** — established by state legislature
- **Deemed Universities** — institutions granted autonomy by UGC
- **Private Universities** — established by state acts
- **Institutions of National Importance** — IITs, IIMs, AIIMS, NITs

## Conventional vs Non-conventional Learning

| Mode | Description |
|------|-------------|
| **Conventional** | Regular classroom, full-time, campus-based |
| **Distance Education** | IGNOU — flexible, self-paced learning |
| **Online/e-Learning** | MOOCs, virtual classrooms |
| **Blended Learning** | Mix of face-to-face and online |

## Value Education and Vocational Education

- **Value Education** — Ethics, integrity, social responsibility
- **Vocational Education** — Skill-based, employment-oriented training
- **NEP 2020** mandates integration of vocational courses from Class 6
""",
            },
        ],
        'questions': [
            {
                'question_text': 'Which ancient Indian university was a famous centre of Buddhist learning in Bihar?',
                'option_a': 'Takshashila', 'option_b': 'Nalanda', 'option_c': 'Vallabhi', 'option_d': 'Vikramashila',
                'correct_answer': 'B', 'difficulty': 'medium',
                'explanation': 'Nalanda University in Bihar (5th–12th century CE) was the most famous ancient centre of Buddhist higher learning, attracting scholars from across Asia.'
            },
            {
                'question_text': 'The Kothari Commission (1964–66) recommended spending what percentage of GDP on education?',
                'option_a': '4%', 'option_b': '8%', 'option_c': '6%', 'option_d': '10%',
                'correct_answer': 'C', 'difficulty': 'medium',
                'explanation': 'The Kothari Commission recommended allocating 6% of GDP to education, a target that India has yet to fully achieve.'
            },
            {
                'question_text': 'Which body is responsible for accrediting higher education institutions in India?',
                'option_a': 'UGC', 'option_b': 'AICTE', 'option_c': 'NAAC', 'option_d': 'NIRF',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'NAAC (National Assessment and Accreditation Council) is responsible for assessing and accrediting higher education institutions in India.'
            },
            {
                'question_text': 'NEP 2020 targets what percentage of Gross Enrolment Ratio (GER) in higher education by 2035?',
                'option_a': '30%', 'option_b': '40%', 'option_c': '60%', 'option_d': '50%',
                'correct_answer': 'D', 'difficulty': 'medium',
                'explanation': 'NEP 2020 aims to increase the Gross Enrolment Ratio (GER) in higher education to 50% by 2035.'
            },
        ]
    },

]  # end PAPER1_SUBJECTS

# ══════════════════════════════════════════════════════
#  PAPER 2  —  Computer Science & IT  (10 Units)
# ══════════════════════════════════════════════════════

PAPER2_SUBJECTS = [

    # ── Unit 1: Discrete Mathematics & Graph Theory ─────
    {
        'name': 'Discrete Mathematics & Graph Theory',
        'icon': '📐', 'color': '#1e40af',
        'description': 'Sets, relations, functions, logic, combinatorics, and graph theory',
        'topics': [
            {
                'title': 'Sets, Relations and Functions',
                'summary': 'Foundational concepts of discrete mathematics: set operations, relations, and types of functions.',
                'difficulty': 'medium', 'estimated_minutes': 40,
                'content': """## Sets

A **set** is a well-defined collection of distinct objects.

### Set Operations
| Operation | Symbol | Meaning |
|-----------|--------|---------|
| Union | A ∪ B | Elements in A or B (or both) |
| Intersection | A ∩ B | Elements in both A and B |
| Difference | A − B | Elements in A but not in B |
| Complement | A' or Ā | Elements not in A (within universal set) |
| Symmetric Difference | A ⊕ B | (A−B) ∪ (B−A) |

### Set Laws
- **De Morgan's Laws:** (A ∪ B)' = A' ∩ B' and (A ∩ B)' = A' ∪ B'
- **Distributive:** A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)

### Cardinality (Inclusion-Exclusion Principle)
|A ∪ B| = |A| + |B| − |A ∩ B|

## Relations

A **relation** R from set A to set B is a subset of A × B.

### Properties of Relations
| Property | Definition |
|----------|-----------|
| **Reflexive** | (a,a) ∈ R for all a ∈ A |
| **Symmetric** | If (a,b) ∈ R then (b,a) ∈ R |
| **Antisymmetric** | If (a,b) and (b,a) ∈ R then a=b |
| **Transitive** | If (a,b) and (b,c) ∈ R then (a,c) ∈ R |

**Equivalence Relation** = Reflexive + Symmetric + Transitive
**Partial Order** = Reflexive + Antisymmetric + Transitive

## Functions

A **function** f: A → B assigns exactly one element of B to each element of A.

### Types of Functions
- **Injective (One-to-one):** Different inputs → different outputs
- **Surjective (Onto):** Every element of B is mapped to
- **Bijective:** Both injective and surjective (one-to-one correspondence)

## Combinatorics

### Permutations and Combinations
- **Permutation (order matters):** P(n,r) = n! / (n−r)!
- **Combination (order doesn't matter):** C(n,r) = n! / [r!(n−r)!]

### Pigeonhole Principle
If n+1 objects are placed in n boxes, at least one box contains ≥2 objects.
""",
            },
            {
                'title': 'Graph Theory Fundamentals',
                'summary': 'Graphs, trees, paths, connectivity, and graph algorithms essential for CS examinations.',
                'difficulty': 'hard', 'estimated_minutes': 45,
                'content': """## Graphs

A **graph** G = (V, E) consists of a set of vertices V and edges E.

### Types of Graphs
| Type | Description |
|------|-------------|
| **Undirected** | Edges have no direction |
| **Directed (Digraph)** | Edges have direction |
| **Weighted** | Edges have weights/costs |
| **Complete (Kₙ)** | Every vertex connected to every other |
| **Bipartite** | Vertices split into two sets; edges only between sets |
| **Planar** | Can be drawn on a plane without crossing edges |

### Graph Terminology
- **Degree** — number of edges incident to a vertex
- **In-degree / Out-degree** — for directed graphs
- **Path** — sequence of vertices connected by edges
- **Cycle** — path that starts and ends at the same vertex
- **Connected Graph** — path exists between every pair of vertices

### Key Theorems
- **Handshaking Lemma:** Sum of all degrees = 2|E|
- **Euler's Formula (Planar):** V − E + F = 2

## Trees

A **tree** is a connected acyclic undirected graph.

### Properties of a Tree with n vertices:
- Has exactly **n−1 edges**
- Is **connected** with no cycles
- Has a unique path between any two vertices

### Types of Trees
- **Rooted Tree** — one vertex designated as root
- **Binary Tree** — each node has at most 2 children
- **Spanning Tree** — subgraph that is a tree including all vertices
- **Minimum Spanning Tree (MST)** — spanning tree with minimum total edge weight

### MST Algorithms
- **Kruskal's** — sort edges by weight, add if no cycle
- **Prim's** — grow tree from a starting vertex, always pick minimum weight edge

## Graph Traversals
- **BFS (Breadth-First Search)** — explores level by level using a queue
- **DFS (Depth-First Search)** — explores as deep as possible using a stack/recursion

## Euler and Hamiltonian Paths
| Type | Condition |
|------|-----------|
| **Euler Path** | Visits every edge exactly once |
| **Euler Circuit** | Euler path starting/ending at same vertex |
| **Hamiltonian Path** | Visits every vertex exactly once |
| **Hamiltonian Circuit** | Hamiltonian path starting/ending at same vertex |

**Euler Circuit exists** ↔ graph is connected and every vertex has even degree.
""",
            },
        ],
        'questions': [
            {
                'question_text': 'De Morgan\'s law states that (A ∪ B)\' equals:',
                'option_a': "A' ∪ B'", 'option_b': "A' ∩ B'", 'option_c': "A ∩ B", 'option_d': "A ∪ B",
                'correct_answer': 'B', 'difficulty': 'easy',
                'explanation': "De Morgan's Law: (A ∪ B)' = A' ∩ B'. The complement of a union is the intersection of complements."
            },
            {
                'question_text': 'A relation that is reflexive, symmetric, and transitive is called:',
                'option_a': 'Partial Order', 'option_b': 'Total Order',
                'option_c': 'Equivalence Relation', 'option_d': 'Antisymmetric Relation',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'An equivalence relation has all three properties: reflexive, symmetric, and transitive.'
            },
            {
                'question_text': 'The number of edges in a tree with n vertices is:',
                'option_a': 'n', 'option_b': 'n+1', 'option_c': 'n−1', 'option_d': '2n',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'A tree with n vertices always has exactly n−1 edges. This is a fundamental property of trees.'
            },
            {
                'question_text': 'An Euler Circuit exists in a graph if and only if:',
                'option_a': 'All vertices have odd degree',
                'option_b': 'The graph is connected and all vertices have even degree',
                'option_c': 'The graph is a complete graph',
                'option_d': 'All vertices have degree ≥ 2',
                'correct_answer': 'B', 'difficulty': 'medium',
                'explanation': 'An Euler Circuit exists if and only if the graph is connected and every vertex has an even degree.'
            },
        ]
    },

    # ── Unit 2: Computer Organisation & Architecture ────
    {
        'name': 'Computer Organisation & Architecture',
        'icon': '🖥️', 'color': '#374151',
        'description': 'CPU design, memory hierarchy, instruction sets, pipelining and I/O systems',
        'topics': [
            {
                'title': 'CPU Organisation and Instruction Sets',
                'summary': 'Internal structure of the CPU, register organisation, instruction formats and addressing modes.',
                'difficulty': 'hard', 'estimated_minutes': 50,
                'content': """## Von Neumann Architecture

The classical computer architecture consisting of:
- **CPU** (Control Unit + ALU)
- **Memory** (single shared memory for instructions and data)
- **Input/Output devices**
- **Bus system** connecting all components

## Components of the CPU

### 1. Arithmetic Logic Unit (ALU)
Performs arithmetic (+, −, ×, ÷) and logical (AND, OR, NOT, XOR) operations.

### 2. Control Unit (CU)
- Fetches, decodes, and executes instructions
- Controls data flow between CPU, memory, and I/O

### 3. Registers
| Register | Function |
|----------|----------|
| **PC (Program Counter)** | Holds address of next instruction |
| **IR (Instruction Register)** | Holds current instruction |
| **MAR (Memory Address Register)** | Holds address to read/write |
| **MDR (Memory Data Register)** | Holds data read from/written to memory |
| **ACC (Accumulator)** | Temporary result storage |

## Instruction Cycle (Fetch-Decode-Execute)

1. **Fetch** — PC → MAR, Memory → MDR → IR, PC incremented
2. **Decode** — CU interprets the opcode in IR
3. **Execute** — ALU performs operation, results stored

## Instruction Format

```
| Opcode | Operand 1 | Operand 2 |
```

### Types of Instructions
- **Zero-address** — stack-based (PUSH, POP)
- **One-address** — one explicit operand (accumulator implied)
- **Two-address** — two explicit operands
- **Three-address** — source1, source2, destination all explicit

## Addressing Modes
| Mode | Description | Example |
|------|-------------|---------|
| **Immediate** | Operand is the data itself | ADD #5 |
| **Direct** | Operand is memory address | ADD 1000 |
| **Indirect** | Address contains pointer to data | ADD (1000) |
| **Register** | Operand in a register | ADD R1 |
| **Register Indirect** | Register holds memory address | ADD (R1) |
| **Indexed** | Base + Index register | ADD 1000(R1) |
| **Relative** | PC + offset | BEQ 20 |

## RISC vs CISC

| Feature | RISC | CISC |
|---------|------|------|
| Instructions | Simple, few | Complex, many |
| Instruction size | Fixed | Variable |
| Cycles per instruction | ~1 | Multiple |
| Examples | ARM, MIPS, SPARC | Intel x86 |
""",
            },
            {
                'title': 'Memory Hierarchy and Pipelining',
                'summary': 'Memory types, cache, virtual memory, and CPU pipelining for performance improvement.',
                'difficulty': 'hard', 'estimated_minutes': 45,
                'content': """## Memory Hierarchy

```
Registers (fastest, smallest)
    ↓
Cache (L1, L2, L3)
    ↓
Main Memory (RAM)
    ↓
Secondary Storage (HDD, SSD)
    ↓
Tertiary Storage (slowest, largest)
```

### Cache Memory
- Small, fast memory between CPU and RAM
- Uses **principle of locality:**
  - **Temporal locality** — recently used data likely used again
  - **Spatial locality** — nearby data likely used soon

### Cache Mapping
| Method | Description |
|--------|-------------|
| **Direct Mapping** | Each block maps to exactly one cache line |
| **Fully Associative** | Any block can go in any cache line |
| **Set Associative** | Compromise — blocks map to a set of lines |

### Cache Replacement Policies
- **LRU (Least Recently Used)** — replace oldest unused block
- **FIFO** — replace first-loaded block
- **LFU (Least Frequently Used)** — replace least accessed block

## Virtual Memory

- Allows execution of programs larger than physical RAM
- Uses **page table** to map virtual addresses to physical addresses
- **Page Fault** — required page not in RAM, must be loaded from disk

### Page Replacement Algorithms
- **FIFO** — replace the oldest page
- **LRU** — replace least recently used page
- **Optimal** — replace page not needed for longest time (theoretical)

### Thrashing
Occurs when system spends more time swapping pages than executing — caused by too little physical memory.

## Pipelining

**Pipelining** divides instruction execution into stages, allowing overlapping of stages.

### Classic 5-Stage RISC Pipeline
1. **IF** — Instruction Fetch
2. **ID** — Instruction Decode
3. **EX** — Execute
4. **MEM** — Memory Access
5. **WB** — Write Back

### Pipeline Performance
- **Throughput** ≈ 1 instruction per cycle (ideally)
- **Speedup** = n × k / (k + n − 1) where n = instructions, k = stages

### Pipeline Hazards
| Hazard | Cause | Solution |
|--------|-------|---------|
| **Structural** | Hardware conflict | Stall, duplicate hardware |
| **Data** | RAW, WAW, WAR dependencies | Forwarding, stall |
| **Control** | Branch instructions | Branch prediction, delayed branching |
""",
            },
        ],
        'questions': [
            {
                'question_text': 'Which register holds the address of the next instruction to be executed?',
                'option_a': 'Accumulator', 'option_b': 'Instruction Register',
                'option_c': 'Program Counter', 'option_d': 'Memory Data Register',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'The Program Counter (PC) always holds the memory address of the next instruction to be fetched.'
            },
            {
                'question_text': 'In which addressing mode does the instruction contain the actual data value?',
                'option_a': 'Direct', 'option_b': 'Indirect', 'option_c': 'Immediate', 'option_d': 'Register',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'Immediate addressing mode embeds the actual data value directly in the instruction itself.'
            },
            {
                'question_text': 'Which cache replacement policy removes the page that has not been used for the longest time?',
                'option_a': 'FIFO', 'option_b': 'LRU', 'option_c': 'Optimal', 'option_d': 'LFU',
                'correct_answer': 'B', 'difficulty': 'medium',
                'explanation': 'LRU (Least Recently Used) replaces the page/cache block that has not been accessed for the longest duration.'
            },
            {
                'question_text': 'A data hazard in pipelining caused by a later instruction needing the result of an earlier instruction is called:',
                'option_a': 'WAR', 'option_b': 'WAW', 'option_c': 'RAW', 'option_d': 'Structural',
                'correct_answer': 'C', 'difficulty': 'hard',
                'explanation': 'RAW (Read After Write) hazard occurs when an instruction needs to read data that a previous instruction has not yet written — the most common data hazard.'
            },
        ]
    },

    # ── Unit 3: Programming & Data Structures ───────────
    {
        'name': 'Programming & Data Structures',
        'icon': '⌨️', 'color': '#b45309',
        'description': 'C, C++, Java programming; pointers, recursion, arrays, stacks, queues, linked lists',
        'topics': [
            {
                'title': 'C Programming Fundamentals',
                'summary': 'Core C programming concepts including data types, control flow, functions, arrays, and pointers.',
                'difficulty': 'medium', 'estimated_minutes': 45,
                'content': """## C Language Basics

C is a **middle-level, structured, procedural** programming language developed by **Dennis Ritchie** at Bell Labs (1972).

## Data Types in C

| Type | Size | Range |
|------|------|-------|
| `char` | 1 byte | −128 to 127 |
| `int` | 4 bytes | −2³¹ to 2³¹−1 |
| `float` | 4 bytes | ±3.4 × 10³⁸ |
| `double` | 8 bytes | ±1.7 × 10³⁰⁸ |
| `void` | — | No value |

## Control Structures

### Decision Making
```c
if (condition) { ... }
else if (condition) { ... }
else { ... }

switch(expr) {
    case 1: ...; break;
    default: ...;
}
```

### Loops
```c
for (init; condition; update) { ... }
while (condition) { ... }
do { ... } while (condition);
```

## Functions

```c
return_type function_name(parameters) {
    // body
    return value;
}
```

- **Call by Value** — copy of argument passed; original unchanged
- **Call by Reference** — address passed; original can be modified

## Arrays

- **1D Array:** `int arr[10];`
- **2D Array:** `int matrix[3][4];`
- Arrays are stored in **contiguous memory locations**

## Pointers

A pointer stores the **memory address** of a variable.

```c
int x = 10;
int *ptr = &x;    // ptr holds address of x
printf("%d", *ptr); // dereference: prints 10
```

### Pointer Arithmetic
- `ptr + 1` — moves to next element of the type
- `ptr[i]` — equivalent to `*(ptr + i)`

## Dynamic Memory Allocation

```c
int *arr = (int*) malloc(n * sizeof(int));  // allocate
arr = (int*) realloc(arr, new_size);        // resize
free(arr);                                  // deallocate
```

## Structures

```c
struct Student {
    char name[50];
    int roll;
    float gpa;
};
struct Student s1 = {"Alice", 101, 9.5};
```

## Recursion

A function calling itself. Requires:
1. **Base case** — stopping condition
2. **Recursive case** — problem reduced toward base case

```c
int factorial(int n) {
    if (n <= 1) return 1;           // base case
    return n * factorial(n - 1);    // recursive case
}
```
""",
            },
            {
                'title': 'Object-Oriented Programming with C++ and Java',
                'summary': 'OOP concepts — classes, inheritance, polymorphism, encapsulation, and abstraction.',
                'difficulty': 'medium', 'estimated_minutes': 50,
                'content': """## Object-Oriented Programming (OOP)

OOP models programs as collections of **objects** that interact with each other.

## Four Pillars of OOP

### 1. Encapsulation
Bundling data and methods that operate on data within a single unit (class), and restricting access using **access modifiers**.

| Modifier | C++ | Java | Accessible From |
|----------|-----|------|-----------------|
| `public` | ✓ | ✓ | Anywhere |
| `private` | ✓ | ✓ | Class only |
| `protected` | ✓ | ✓ | Class + subclasses |

### 2. Inheritance
A class (child/subclass) inherits properties from another class (parent/superclass).

**C++:** `class Dog : public Animal { ... }`
**Java:** `class Dog extends Animal { ... }`

**Types in C++:**
- Single, Multiple, Multilevel, Hierarchical, Hybrid

**Java:** Supports only **single inheritance** (multiple inheritance via interfaces).

### 3. Polymorphism
Same interface, different implementations.

- **Compile-time (Static):** Method/Operator **Overloading**
  - Same method name, different parameters
- **Run-time (Dynamic):** Method **Overriding**
  - Subclass redefines parent's method; resolved at runtime via virtual functions (C++) / @Override (Java)

### 4. Abstraction
Hiding implementation details; showing only essential features.

- **Abstract Classes** — cannot be instantiated; may have abstract methods
- **Interfaces** — fully abstract (Java: all methods abstract by default pre-Java 8)

## Java Specific Concepts

### Java Memory Model
- **Stack** — method calls, local variables
- **Heap** — objects allocated with `new`

### Java Keywords
- `final` — constant variable / cannot override method / cannot extend class
- `static` — belongs to class, not instance
- `this` — refers to current object
- `super` — refers to parent class

### Exception Handling in Java
```java
try {
    // risky code
} catch (ExceptionType e) {
    // handle
} finally {
    // always executes
}
```

### Common Design Patterns
| Pattern | Category | Purpose |
|---------|----------|---------|
| Singleton | Creational | Only one instance |
| Factory | Creational | Create objects |
| Observer | Behavioral | Event notification |
| Strategy | Behavioral | Interchangeable algorithms |
""",
            },
        ],
        'questions': [
            {
                'question_text': 'Which of the following correctly declares a pointer to an integer in C?',
                'option_a': 'int ptr;', 'option_b': 'int *ptr;', 'option_c': '*int ptr;', 'option_d': 'ptr *int;',
                'correct_answer': 'B', 'difficulty': 'easy',
                'explanation': 'int *ptr; declares a pointer named ptr that points to an integer. The * indicates it is a pointer type.'
            },
            {
                'question_text': 'In Java, which keyword is used to inherit a class?',
                'option_a': 'implements', 'option_b': 'inherits', 'option_c': 'extends', 'option_d': 'super',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'In Java, the "extends" keyword is used for class inheritance: class Child extends Parent { }'
            },
            {
                'question_text': 'Method overloading is an example of which type of polymorphism?',
                'option_a': 'Runtime polymorphism', 'option_b': 'Compile-time polymorphism',
                'option_c': 'Dynamic dispatch', 'option_d': 'Interface polymorphism',
                'correct_answer': 'B', 'difficulty': 'medium',
                'explanation': 'Method overloading is resolved at compile time, making it compile-time (static) polymorphism.'
            },
            {
                'question_text': 'Which function in C is used to dynamically allocate memory?',
                'option_a': 'alloc()', 'option_b': 'new()', 'option_c': 'malloc()', 'option_d': 'memalloc()',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'malloc() (memory allocation) is used in C to dynamically allocate a specified number of bytes on the heap.'
            },
        ]
    },

    # ── Unit 4: Theory of Computation & Compiler Design ─
    {
        'name': 'Theory of Computation & Compiler Design',
        'icon': '⚙️', 'color': '#064e3b',
        'description': 'Automata, formal languages, Turing machines, and phases of compiler design',
        'topics': [
            {
                'title': 'Automata Theory and Formal Languages',
                'summary': 'Finite automata, pushdown automata, Turing machines and Chomsky hierarchy of languages.',
                'difficulty': 'hard', 'estimated_minutes': 55,
                'content': """## Formal Language Hierarchy (Chomsky)

```
Type 0: Recursively Enumerable (RE) — Turing Machines
  Type 1: Context-Sensitive (CSL) — Linear Bounded Automata
    Type 2: Context-Free (CFL) — Pushdown Automata (PDA)
      Type 3: Regular — Finite Automata (DFA/NFA)
```

Each inner set is a strict subset of the outer.

## Regular Languages (Type 3)

### Finite Automata
- **DFA (Deterministic Finite Automaton)** — exactly one transition per (state, symbol)
- **NFA (Non-deterministic Finite Automaton)** — zero or more transitions; ε-moves allowed

**Key result:** DFA and NFA are equivalent in power — every NFA has an equivalent DFA.

### Regular Expressions
- `a*` — zero or more 'a'
- `a+` — one or more 'a'
- `a|b` — 'a' or 'b'
- `a?` — zero or one 'a'
- `(ab)*` — zero or more repetitions of "ab"

### Closure Properties of Regular Languages
Regular languages are closed under: Union, Concatenation, Kleene Star, Complementation, Intersection.

### Pumping Lemma (Regular)
Used to prove a language is NOT regular.
If L is regular, there exists p such that any string w in L with |w| ≥ p can be written as xyz where:
- |y| ≥ 1
- |xy| ≤ p
- xyⁿz ∈ L for all n ≥ 0

## Context-Free Languages (Type 2)

### Context-Free Grammars (CFG)
Productions of the form: A → α (A is a single non-terminal; α is any string)

**Example:** S → aSb | ε generates {aⁿbⁿ | n ≥ 0}

### Pushdown Automata (PDA)
Finite automaton with a **stack** — can recognise CFLs.

### Ambiguity
A grammar is **ambiguous** if some string has two or more distinct parse trees (derivations).

## Turing Machines (Type 0)

- Has an infinite tape, read-write head, and transition function
- Most powerful model of computation
- **Church-Turing Thesis:** Any effectively computable function can be computed by a TM

### Decidability
- **Decidable (Recursive)** — TM always halts with yes/no
- **Semi-decidable (RE)** — TM halts on "yes" but may loop on "no"
- **Undecidable** — No TM can solve it

**Halting Problem** — Undecidable (proved by Alan Turing, 1936)
""",
            },
            {
                'title': 'Compiler Design: Phases and Parsing',
                'summary': 'Phases of a compiler, lexical analysis, parsing techniques, and code generation.',
                'difficulty': 'hard', 'estimated_minutes': 50,
                'content': """## Phases of a Compiler

```
Source Code
    ↓
[1] Lexical Analysis (Scanner)
    ↓ Tokens
[2] Syntax Analysis (Parser)
    ↓ Parse Tree / AST
[3] Semantic Analysis
    ↓ Annotated AST
[4] Intermediate Code Generation
    ↓ IR (e.g., Three-address code)
[5] Code Optimization
    ↓ Optimized IR
[6] Code Generation
    ↓
Target Code (Machine Code)
```

## Phase 1: Lexical Analysis

- Reads source code character by character
- Groups characters into **tokens** (keywords, identifiers, literals, operators)
- Removes whitespace and comments
- Implemented using **Finite Automata and Regular Expressions**
- Tool: **lex / flex**

**Token types:** keyword, identifier, constant, operator, punctuation

## Phase 2: Syntax Analysis (Parsing)

Checks if the token sequence follows the grammar of the language.

### Types of Parsers

**Top-Down Parsing:**
- Starts from start symbol, tries to derive the input
- **Recursive Descent Parser** — recursive functions for each non-terminal
- **LL(k) Parser** — reads Left-to-right, Leftmost derivation, k lookahead tokens

**Bottom-Up Parsing:**
- Starts from input, reduces to start symbol
- **LR(k) Parser** — reads Left-to-right, Rightmost derivation in reverse
- **SLR, LALR, CLR** — variants with different power/complexity
- **LALR** is most commonly used (e.g., YACC/Bison)

### First and Follow Sets
- **FIRST(A)** — set of terminals that can begin strings derived from A
- **FOLLOW(A)** — set of terminals that can appear after A in some sentential form

## Phase 3: Semantic Analysis

- Checks meaning/consistency: type checking, scope rules
- Uses **Symbol Table** to track identifiers, types, scopes

## Intermediate Code

Three-address code example:
```
t1 = a + b
t2 = t1 * c
x = t2
```

## Code Optimization Techniques

- **Constant Folding:** Evaluate constant expressions at compile time (2+3 → 5)
- **Dead Code Elimination:** Remove code that never executes
- **Loop Invariant Code Motion:** Move code outside loops
- **Common Subexpression Elimination:** Reuse previously computed values
""",
            },
        ],
        'questions': [
            {
                'question_text': 'Which automaton can recognise Context-Free Languages?',
                'option_a': 'Finite Automaton', 'option_b': 'Pushdown Automaton',
                'option_c': 'Linear Bounded Automaton', 'option_d': 'Turing Machine',
                'correct_answer': 'B', 'difficulty': 'easy',
                'explanation': 'Pushdown Automata (PDA) recognize Context-Free Languages. They are equivalent to CFGs in expressive power.'
            },
            {
                'question_text': 'The Halting Problem is:',
                'option_a': 'Decidable', 'option_b': 'Context-Free', 'option_c': 'Undecidable', 'option_d': 'In the class NP-Complete',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'The Halting Problem was proven undecidable by Alan Turing in 1936 — no algorithm can always determine if a program halts.'
            },
            {
                'question_text': 'Which phase of a compiler converts source code into tokens?',
                'option_a': 'Syntax Analysis', 'option_b': 'Semantic Analysis',
                'option_c': 'Lexical Analysis', 'option_d': 'Code Generation',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'Lexical Analysis (scanning) is the first phase — it reads characters and groups them into tokens (keywords, identifiers, etc.).'
            },
            {
                'question_text': 'LALR parsers are a type of:',
                'option_a': 'Top-down parsers', 'option_b': 'Recursive descent parsers',
                'option_c': 'Bottom-up parsers', 'option_d': 'Backtracking parsers',
                'correct_answer': 'C', 'difficulty': 'medium',
                'explanation': 'LALR (Look-Ahead LR) parsers are bottom-up parsers and are the most commonly used parser type in practice (used by YACC/Bison).'
            },
        ]
    },

    # ── Unit 5: Data Structures & Algorithms ────────────
    {
        'name': 'Data Structures & Algorithms',
        'icon': '🗂️', 'color': '#7c3aed',
        'description': 'Arrays, linked lists, stacks, queues, trees, heaps, hashing, sorting, searching, complexity',
        'topics': [
            {
                'title': 'Arrays, Linked Lists, Stacks and Queues',
                'summary': 'Fundamental linear data structures and their operations, trade-offs and applications.',
                'difficulty': 'medium', 'estimated_minutes': 45,
                'content': """## Arrays

Contiguous block of memory storing elements of the same type.

| Operation | Time Complexity |
|-----------|----------------|
| Access by index | O(1) |
| Search (unsorted) | O(n) |
| Search (sorted, binary search) | O(log n) |
| Insert/Delete (middle) | O(n) |

## Linked Lists

A sequence of **nodes**, each containing data and a pointer to the next node.

### Types
| Type | Description |
|------|-------------|
| **Singly Linked List** | Each node → next node |
| **Doubly Linked List** | Each node → next and previous |
| **Circular Linked List** | Last node → first node |

### Operations

| Operation | SLL Time |
|-----------|----------|
| Insert at beginning | O(1) |
| Insert at end (with tail) | O(1) |
| Delete at beginning | O(1) |
| Search | O(n) |
| Access by position | O(n) |

### Array vs Linked List

| Feature | Array | Linked List |
|---------|-------|-------------|
| Memory | Static/contiguous | Dynamic/scattered |
| Access | O(1) random | O(n) sequential |
| Insert/Delete | O(n) | O(1) at known position |
| Memory overhead | Less | More (pointers) |

## Stack

**LIFO (Last In, First Out)** data structure.

### Operations (all O(1))
- `push(x)` — add element to top
- `pop()` — remove and return top element
- `peek()/top()` — return top without removing
- `isEmpty()` — check if stack is empty

### Applications
- Function call stack
- Expression evaluation and conversion (infix ↔ postfix)
- Undo/Redo operations
- Backtracking algorithms
- Balanced parenthesis checking

## Queue

**FIFO (First In, First Out)** data structure.

### Operations (all O(1))
- `enqueue(x)` — add element to rear
- `dequeue()` — remove element from front
- `front()` — peek at front element

### Types of Queues
- **Simple Queue** — basic FIFO
- **Circular Queue** — front and rear wrap around
- **Priority Queue** — elements with higher priority dequeued first
- **Deque (Double-ended Queue)** — insert/delete at both ends

### Applications
- CPU scheduling
- Breadth-First Search (BFS)
- Print spooling
- Keyboard buffer
""",
            },
            {
                'title': 'Trees, Heaps and Hashing',
                'summary': 'Binary search trees, AVL trees, heap operations, and hash table collision resolution.',
                'difficulty': 'hard', 'estimated_minutes': 50,
                'content': """## Binary Search Tree (BST)

For every node:
- **Left subtree** contains only nodes with **smaller** keys
- **Right subtree** contains only nodes with **larger** keys

### BST Operations
| Operation | Average | Worst (skewed) |
|-----------|---------|----------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |

### BST Traversals
- **Inorder (LNR)** → sorted sequence
- **Preorder (NLR)** → copy tree
- **Postorder (LRN)** → delete tree

## AVL Tree (Self-balancing BST)

Balance Factor = height(left subtree) − height(right subtree)
**Must be −1, 0, or +1** for every node.

### Rotations to Restore Balance
| Case | Rotation |
|------|----------|
| Left-Left (LL) | Right Rotation |
| Right-Right (RR) | Left Rotation |
| Left-Right (LR) | Left then Right Rotation |
| Right-Left (RL) | Right then Left Rotation |

**Guaranteed O(log n)** for all operations.

## Heap

A **complete binary tree** satisfying the heap property:
- **Max-Heap** — parent ≥ children (root is maximum)
- **Min-Heap** — parent ≤ children (root is minimum)

### Heap Operations
| Operation | Time |
|-----------|------|
| Insert | O(log n) |
| Extract Max/Min | O(log n) |
| Build Heap | O(n) |
| Peek (max/min) | O(1) |

### Applications
- **Priority Queue** implementation
- **Heap Sort** — O(n log n)
- **Dijkstra's** shortest path algorithm

## Hashing

Maps keys to indices in a hash table using a **hash function**.

### Hash Function Properties
- Deterministic
- Uniform distribution
- Fast to compute

### Collision Resolution

**1. Chaining (Open Hashing)**
- Each table slot holds a linked list of all keys that hash to it
- Average search: O(1 + α) where α = load factor = n/m

**2. Open Addressing (Closed Hashing)**
- All elements stored in the table itself
- **Linear Probing:** Try h(k)+1, h(k)+2, ... (causes clustering)
- **Quadratic Probing:** Try h(k)+1², h(k)+2², ...
- **Double Hashing:** Use a second hash function

### Load Factor (α)
- α = number of entries / table size
- α < 0.7 recommended for performance
""",
            },
            {
                'title': 'Sorting, Searching and Algorithm Complexity',
                'summary': 'Major sorting algorithms, binary search, and Big-O complexity analysis.',
                'difficulty': 'medium', 'estimated_minutes': 45,
                'content': """## Algorithm Complexity

### Big-O Notation
Describes the **worst-case** growth rate of an algorithm.

| Complexity | Name | Example |
|------------|------|---------|
| O(1) | Constant | Array access |
| O(log n) | Logarithmic | Binary Search |
| O(n) | Linear | Linear Search |
| O(n log n) | Linearithmic | Merge Sort |
| O(n²) | Quadratic | Bubble Sort |
| O(2ⁿ) | Exponential | Subset generation |
| O(n!) | Factorial | Permutations |

### Recurrence Relations
- **Master Theorem:** T(n) = aT(n/b) + f(n)

## Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable? |
|-----------|------|---------|-------|-------|---------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | No |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| **Radix Sort** | O(nk) | O(nk) | O(nk) | O(n+k) | Yes |

**Stable sort:** Equal elements maintain their original relative order.

## Key Sorting Concepts

### Merge Sort
Divide-and-conquer; always O(n log n); best for linked lists.

### Quick Sort
Pivot selection → partition → recurse.
- **Best pivot:** Median of array
- **Worst case:** Already sorted array with first/last pivot

### Counting Sort / Radix Sort
Non-comparison based; O(n+k) where k = range of keys.

## Searching Algorithms

### Linear Search
- Sequentially checks each element
- Time: O(n); works on unsorted data

### Binary Search
- Requires **sorted** array
- Time: O(log n)
- Process: Compare with middle → eliminate half → repeat

```
mid = (low + high) / 2
if arr[mid] == key: found
elif arr[mid] < key: search right half
else: search left half
```
""",
            },
        ],
        'questions': [
            {
                'question_text': 'Which data structure follows the LIFO principle?',
                'option_a': 'Queue', 'option_b': 'Stack', 'option_c': 'Linked List', 'option_d': 'Deque',
                'correct_answer': 'B', 'difficulty': 'easy',
                'explanation': 'Stack follows the LIFO (Last In, First Out) principle — the last element inserted is the first to be removed.'
            },
            {
                'question_text': 'What is the time complexity of binary search on a sorted array?',
                'option_a': 'O(n)', 'option_b': 'O(n²)', 'option_c': 'O(log n)', 'option_d': 'O(1)',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'Binary search eliminates half the remaining elements at each step, resulting in O(log n) time complexity.'
            },
            {
                'question_text': 'Which sorting algorithm has the best worst-case time complexity?',
                'option_a': 'Quick Sort', 'option_b': 'Bubble Sort',
                'option_c': 'Merge Sort', 'option_d': 'Selection Sort',
                'correct_answer': 'C', 'difficulty': 'medium',
                'explanation': 'Merge Sort guarantees O(n log n) in all cases (best, average, worst), making it better than Quick Sort\'s O(n²) worst case.'
            },
            {
                'question_text': 'In an AVL tree, the balance factor of every node must be:',
                'option_a': '0 only', 'option_b': '-1, 0, or 1', 'option_c': '-2 to 2', 'option_d': 'Any positive value',
                'correct_answer': 'B', 'difficulty': 'medium',
                'explanation': 'AVL trees maintain balance by ensuring the balance factor (height difference of left and right subtrees) is -1, 0, or +1 at every node.'
            },
            {
                'question_text': 'The inorder traversal of a BST produces:',
                'option_a': 'Reverse sorted sequence', 'option_b': 'Random sequence',
                'option_c': 'Level-order sequence', 'option_d': 'Sorted sequence',
                'correct_answer': 'D', 'difficulty': 'easy',
                'explanation': 'Inorder traversal (Left-Node-Right) of a BST always produces elements in ascending (sorted) order.'
            },
        ]
    },

    # ── Unit 6: Operating Systems ────────────────────────
    {
        'name': 'Operating Systems',
        'icon': '🐧', 'color': '#1f2937',
        'description': 'Process management, scheduling, memory management, file systems, deadlocks and concurrency',
        'topics': [
            {
                'title': 'Process Management and CPU Scheduling',
                'summary': 'Process states, PCB, CPU scheduling algorithms and their performance metrics.',
                'difficulty': 'medium', 'estimated_minutes': 45,
                'content': """## What is a Process?

A **process** is a program in execution. It includes:
- Program code (text section)
- Current activity (program counter, registers)
- Stack (function parameters, return addresses, local variables)
- Data section (global variables)
- Heap (dynamically allocated memory)

## Process States

```
New → Ready → Running → Terminated
               ↑  ↓
              Waiting/Blocked
```

## Process Control Block (PCB)

Each process is represented by a PCB containing:
- Process ID (PID)
- Process state
- Program counter
- CPU registers
- Memory management information
- I/O status

## CPU Scheduling Algorithms

### Non-Preemptive Algorithms
**1. FCFS (First Come First Served)**
- Processes scheduled in arrival order
- Convoy Effect: short processes wait behind long ones

**2. SJF (Shortest Job First)**
- Process with shortest burst time runs next
- Optimal average waiting time (non-preemptive)

### Preemptive Algorithms
**3. SRTF (Shortest Remaining Time First)**
- Preemptive version of SJF

**4. Round Robin (RR)**
- Each process gets a fixed **time quantum** (q)
- After quantum expires, next process runs
- Fair; best for time-sharing systems

**5. Priority Scheduling**
- Highest priority process runs first
- **Starvation** — low priority processes may never run
- Solution: **Aging** (gradually increase priority of waiting processes)

### Scheduling Metrics
- **Turnaround Time (TAT)** = Completion Time − Arrival Time
- **Waiting Time (WT)** = TAT − Burst Time
- **Response Time** = First CPU access − Arrival Time
- **Throughput** = Number of processes completed per unit time

## Threads

A **thread** is a lightweight process — unit of CPU execution within a process.

- **User-level threads** — managed by user-space library
- **Kernel-level threads** — managed by OS
- Threads within a process share: code, data, heap, files
- Threads have their own: stack, registers, program counter
""",
            },
            {
                'title': 'Deadlocks, Concurrency and Synchronisation',
                'summary': 'Deadlock conditions, prevention/avoidance strategies, and process synchronisation mechanisms.',
                'difficulty': 'hard', 'estimated_minutes': 50,
                'content': """## Concurrency and Race Conditions

**Race Condition:** Two or more processes access shared data concurrently, and the outcome depends on the execution order.

**Critical Section:** The section of code that accesses shared resources.

### Requirements for Critical Section Solution
1. **Mutual Exclusion** — only one process in CS at a time
2. **Progress** — if no process is in CS, a process that wants to enter can
3. **Bounded Waiting** — a process can only wait a finite number of times

## Synchronisation Mechanisms

### 1. Mutex (Mutual Exclusion Lock)
- Binary lock — locked or unlocked
- `acquire()` → enter CS → `release()`

### 2. Semaphore
- Integer variable S, accessed via atomic operations:
  - `wait(S)` — P operation: decrement S; if S < 0, block
  - `signal(S)` — V operation: increment S; wake sleeping process
- **Binary Semaphore** — 0 or 1 (like mutex)
- **Counting Semaphore** — can be any non-negative integer

### 3. Monitor
- High-level synchronisation construct with built-in mutual exclusion
- Only one process active in monitor at a time

## Classical Synchronisation Problems

| Problem | Solution |
|---------|---------|
| **Producer-Consumer** | Two semaphores (full, empty) + mutex |
| **Readers-Writers** | Readers can share; writers need exclusive access |
| **Dining Philosophers** | 5 philosophers, 5 forks — avoid deadlock |

## Deadlock

**Deadlock:** A set of processes are blocked, each waiting for a resource held by another.

### Four Necessary Conditions (Coffman Conditions)
1. **Mutual Exclusion** — resource held by only one process
2. **Hold and Wait** — process holds a resource and waits for more
3. **No Preemption** — resources cannot be forcibly taken
4. **Circular Wait** — circular chain of processes, each waiting for next

### Deadlock Strategies
| Strategy | Approach |
|----------|---------|
| **Prevention** | Eliminate ≥1 Coffman conditions |
| **Avoidance** | Banker's Algorithm — check safe state before allocation |
| **Detection** | Allow deadlock, then detect and recover |
| **Ignorance** | Ostrich Algorithm — pretend it doesn't happen |

### Banker's Algorithm
- Checks if a resource allocation leaves the system in a **safe state**
- Safe state → there exists a safe sequence of process completion
""",
            },
            {
                'title': 'File Systems and Storage Management',
                'summary': 'File system structures, directory organisation, disk scheduling and storage allocation.',
                'difficulty': 'medium', 'estimated_minutes': 40,
                'content': """## File System Concepts

### File Attributes
- Name, type, size, location, creation/modification date, permissions

### File Operations
- Create, Open, Read, Write, Seek, Delete, Close

### File Types
- **Text files** — ASCII/UTF-8 encoded
- **Binary files** — executable, object files
- **Directory files** — contains file entries

## Directory Structures

| Structure | Description |
|-----------|-------------|
| **Single-level** | One directory for all users |
| **Two-level** | Separate directory per user |
| **Tree-structured** | Hierarchical (Unix/Windows) |
| **Acyclic Graph** | Allows shared files/directories |
| **General Graph** | Links may create cycles |

## File Allocation Methods

### 1. Contiguous Allocation
- Files stored in consecutive disk blocks
- ✅ Fast sequential and random access
- ❌ External fragmentation, difficult to grow files

### 2. Linked Allocation
- Each block contains pointer to next block
- ✅ No external fragmentation, easy to grow
- ❌ Slow random access, pointer overhead

### 3. Indexed Allocation
- Index block holds pointers to all data blocks
- ✅ Fast random access, no external fragmentation
- ❌ Overhead of index block

**Unix inode** — form of indexed allocation.

## Disk Scheduling Algorithms

Goal: Minimise seek time (moving disk arm to the right track)

| Algorithm | Strategy |
|-----------|---------|
| **FCFS** | Service requests in arrival order |
| **SSTF (Shortest Seek Time First)** | Service nearest request |
| **SCAN (Elevator)** | Move arm in one direction, serve all, reverse |
| **C-SCAN** | Move in one direction only, reset to start |
| **LOOK** | Like SCAN but reverses at last request |

## Access Control and Security

- **Access Control Matrix** — defines who can do what on which file
- **Access Control List (ACL)** — per-file list of (user, permissions)
- **UNIX Permissions:** rwx for Owner, Group, Others
""",
            },
        ],
        'questions': [
            {
                'question_text': 'Which CPU scheduling algorithm can suffer from the "convoy effect"?',
                'option_a': 'Round Robin', 'option_b': 'Priority Scheduling',
                'option_c': 'FCFS', 'option_d': 'SRTF',
                'correct_answer': 'C', 'difficulty': 'medium',
                'explanation': 'FCFS suffers from the convoy effect — short processes must wait behind a long process, increasing average waiting time.'
            },
            {
                'question_text': 'Which of the following is NOT a necessary condition for deadlock?',
                'option_a': 'Mutual Exclusion', 'option_b': 'Circular Wait',
                'option_c': 'Preemption', 'option_d': 'Hold and Wait',
                'correct_answer': 'C', 'difficulty': 'medium',
                'explanation': '"No Preemption" is a Coffman condition for deadlock. The presence of Preemption (being able to take resources away) actually PREVENTS deadlock.'
            },
            {
                'question_text': 'Turnaround Time is defined as:',
                'option_a': 'Burst Time − Waiting Time', 'option_b': 'Completion Time − Arrival Time',
                'option_c': 'Arrival Time − Completion Time', 'option_d': 'Burst Time + Response Time',
                'correct_answer': 'B', 'difficulty': 'easy',
                'explanation': 'Turnaround Time (TAT) = Completion Time − Arrival Time. It measures total time from submission to completion.'
            },
            {
                'question_text': 'The Banker\'s Algorithm is used for:',
                'option_a': 'Deadlock detection', 'option_b': 'Deadlock prevention',
                'option_c': 'Deadlock avoidance', 'option_d': 'Deadlock recovery',
                'correct_answer': 'C', 'difficulty': 'medium',
                'explanation': 'The Banker\'s Algorithm is a deadlock avoidance algorithm — it checks whether allocating resources will leave the system in a safe state.'
            },
        ]
    },

    # ── Unit 7: Database Management Systems ─────────────
    {
        'name': 'Database Management Systems',
        'icon': '🗄️', 'color': '#9a3412',
        'description': 'Relational model, SQL, normalisation, transactions, ER model and query processing',
        'topics': [
            {
                'title': 'Relational Model, ER Model and SQL',
                'summary': 'Entity-Relationship model, relational algebra, and comprehensive SQL for UGC NET.',
                'difficulty': 'medium', 'estimated_minutes': 50,
                'content': """## Entity-Relationship (ER) Model

Used to design the **conceptual structure** of a database.

### ER Components
| Symbol | Represents |
|--------|-----------|
| Rectangle | Entity |
| Ellipse | Attribute |
| Diamond | Relationship |
| Double rectangle | Weak entity |
| Double ellipse | Multivalued attribute |

### Cardinality of Relationships
- **One-to-One (1:1)** — one student has one ID card
- **One-to-Many (1:N)** — one department has many employees
- **Many-to-Many (M:N)** — students enroll in many courses; courses have many students

### Keys
| Key | Definition |
|-----|-----------|
| **Super Key** | Any set of attributes that uniquely identifies a row |
| **Candidate Key** | Minimal super key |
| **Primary Key** | Chosen candidate key |
| **Foreign Key** | Attribute referencing primary key of another relation |
| **Composite Key** | Primary key using multiple attributes |

## Relational Algebra

| Operation | Symbol | Description |
|-----------|--------|-------------|
| Selection | σ | Filter rows |
| Projection | π | Filter columns |
| Union | ∪ | Combine rows from two tables |
| Intersection | ∩ | Common rows |
| Difference | − | Rows in one but not other |
| Cartesian Product | × | All combinations |
| Join | ⋈ | Natural/Theta/Outer join |

## SQL

### DDL (Data Definition Language)
```sql
CREATE TABLE Student (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    gpa FLOAT DEFAULT 0.0
);
ALTER TABLE Student ADD COLUMN email VARCHAR(100);
DROP TABLE Student;
```

### DML (Data Manipulation Language)
```sql
INSERT INTO Student VALUES (1, 'Alice', 9.5);
UPDATE Student SET gpa = 9.8 WHERE id = 1;
DELETE FROM Student WHERE gpa < 5.0;
```

### DQL (Data Query Language)
```sql
SELECT name, gpa
FROM Student
WHERE gpa > 8.0
ORDER BY gpa DESC
LIMIT 10;
```

### SQL Joins
```sql
-- INNER JOIN: only matching rows
SELECT * FROM A INNER JOIN B ON A.id = B.id;

-- LEFT JOIN: all rows from A, matching from B
SELECT * FROM A LEFT JOIN B ON A.id = B.id;

-- Full Outer Join: all rows from both
SELECT * FROM A FULL OUTER JOIN B ON A.id = B.id;
```

### Aggregate Functions
```sql
SELECT COUNT(*), AVG(gpa), MAX(gpa), MIN(gpa), SUM(gpa)
FROM Student
GROUP BY department
HAVING AVG(gpa) > 8.0;
```
""",
            },
            {
                'title': 'Normalisation and Transactions',
                'summary': 'Database normalisation forms (1NF to BCNF) and ACID properties of transactions.',
                'difficulty': 'hard', 'estimated_minutes': 45,
                'content': """## Functional Dependencies (FD)

**X → Y** means Y is functionally dependent on X — if two rows have the same X value, they must have the same Y value.

### Closure of FDs
Use Armstrong's Axioms:
- **Reflexivity:** Y ⊆ X → X → Y
- **Augmentation:** X → Y → XZ → YZ
- **Transitivity:** X → Y, Y → Z → X → Z

## Normalisation

Process of organising data to reduce **redundancy** and avoid **anomalies** (insert, delete, update anomalies).

### First Normal Form (1NF)
- All attributes are **atomic** (single-valued)
- No repeating groups

### Second Normal Form (2NF)
- Must be in 1NF
- **No partial dependencies** — every non-key attribute must depend on the **entire** composite primary key

### Third Normal Form (3NF)
- Must be in 2NF
- **No transitive dependencies** — non-key attribute must not depend on another non-key attribute

**Rule:** In a relation R, for every FD X → Y:
- X is a superkey, OR
- Y is part of some candidate key

### Boyce-Codd Normal Form (BCNF)
- Must be in 3NF
- Stricter: For every FD X → Y, **X must be a superkey**
- BCNF ⊂ 3NF — every BCNF relation is in 3NF, but not vice versa

## Transactions

A **transaction** is a sequence of operations treated as a single logical unit of work.

### ACID Properties

| Property | Description |
|----------|-------------|
| **Atomicity** | All or nothing — either all operations complete or none do |
| **Consistency** | Database transitions from one valid state to another |
| **Isolation** | Concurrent transactions appear sequential |
| **Durability** | Committed transactions persist even after failures |

## Concurrency Control

### Problems without Concurrency Control
- **Lost Update** — T2 overwrites T1's update
- **Dirty Read** — T2 reads uncommitted data from T1
- **Unrepeatable Read** — T1 reads same data twice, different results
- **Phantom Read** — T1 re-executes query, gets different rows

### Isolation Levels (SQL Standard)
| Level | Dirty Read | Unrepeatable | Phantom |
|-------|-----------|-------------|---------|
| Read Uncommitted | Possible | Possible | Possible |
| Read Committed | Prevented | Possible | Possible |
| Repeatable Read | Prevented | Prevented | Possible |
| Serializable | Prevented | Prevented | Prevented |

### Lock-Based Protocols
- **Shared (S) Lock** — read lock; multiple transactions can hold
- **Exclusive (X) Lock** — write lock; only one transaction
- **Two-Phase Locking (2PL)** — growing phase + shrinking phase; ensures serializability
""",
            },
        ],
        'questions': [
            {
                'question_text': 'Which SQL clause is used to filter groups after a GROUP BY?',
                'option_a': 'WHERE', 'option_b': 'HAVING', 'option_c': 'ORDER BY', 'option_d': 'FILTER',
                'correct_answer': 'B', 'difficulty': 'easy',
                'explanation': 'HAVING filters groups created by GROUP BY, while WHERE filters individual rows before grouping.'
            },
            {
                'question_text': 'A relation is in BCNF if for every functional dependency X → Y:',
                'option_a': 'Y is a prime attribute', 'option_b': 'X is a superkey',
                'option_c': 'X and Y together form the primary key', 'option_d': 'Y is not transitively dependent',
                'correct_answer': 'B', 'difficulty': 'medium',
                'explanation': 'BCNF requires that for every non-trivial FD X → Y, X must be a superkey of the relation.'
            },
            {
                'question_text': 'Which ACID property ensures that a committed transaction\'s changes survive system failures?',
                'option_a': 'Atomicity', 'option_b': 'Consistency', 'option_c': 'Isolation', 'option_d': 'Durability',
                'correct_answer': 'D', 'difficulty': 'easy',
                'explanation': 'Durability ensures that once a transaction is committed, its changes are permanent even in the event of a system crash.'
            },
            {
                'question_text': 'Which join returns all rows from the left table and matching rows from the right table?',
                'option_a': 'INNER JOIN', 'option_b': 'RIGHT JOIN', 'option_c': 'LEFT JOIN', 'option_d': 'CROSS JOIN',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'LEFT JOIN (or LEFT OUTER JOIN) returns all rows from the left table, with NULL values for unmatched rows from the right table.'
            },
        ]
    },

    # ── Unit 8: Computer Networks ────────────────────────
    {
        'name': 'Computer Networks',
        'icon': '🌐', 'color': '#0c4a6e',
        'description': 'OSI model, TCP/IP, protocols, routing, switching, security and wireless networks',
        'topics': [
            {
                'title': 'OSI Model and Network Protocols',
                'summary': 'Seven-layer OSI model, functions of each layer, and key protocols at each level.',
                'difficulty': 'medium', 'estimated_minutes': 50,
                'content': """## OSI Reference Model

The **Open Systems Interconnection (OSI)** model defines a 7-layer framework for network communication.

| Layer | Name | Function | Key Protocols |
|-------|------|----------|---------------|
| 7 | **Application** | User interface, services | HTTP, FTP, SMTP, DNS, DHCP |
| 6 | **Presentation** | Data format, encryption | SSL/TLS, JPEG, MPEG |
| 5 | **Session** | Session management | NetBIOS, RPC |
| 4 | **Transport** | End-to-end communication, reliability | TCP, UDP |
| 3 | **Network** | Routing, logical addressing | IP, ICMP, ARP, RIP, OSPF |
| 2 | **Data Link** | Framing, MAC addressing, error detection | Ethernet, Wi-Fi (802.11), PPP |
| 1 | **Physical** | Bit transmission | RS-232, RJ45, Fiber |

**Mnemonic:** "**P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way"

## TCP/IP Model (4 Layers)

| TCP/IP Layer | Corresponds to OSI |
|-------------|-------------------|
| Application | Application + Presentation + Session |
| Transport | Transport |
| Internet | Network |
| Network Access | Data Link + Physical |

## Key Protocols

### Transport Layer
| Protocol | Type | Features |
|----------|------|---------|
| **TCP** | Connection-oriented | Reliable, ordered, flow control, congestion control |
| **UDP** | Connectionless | Fast, unreliable, no ordering (good for streaming/DNS) |

### Application Layer Protocols
| Protocol | Port | Purpose |
|----------|------|---------|
| HTTP | 80 | Web browsing |
| HTTPS | 443 | Secure web |
| FTP | 20, 21 | File transfer |
| SMTP | 25 | Sending email |
| POP3 | 110 | Receiving email |
| IMAP | 143 | Email management |
| DNS | 53 | Domain name resolution |
| DHCP | 67, 68 | IP address assignment |
| SSH | 22 | Secure shell |
| Telnet | 23 | Remote login (insecure) |

## IP Addressing

### IPv4
- 32-bit address: 4 octets (e.g., 192.168.1.10)
- Classes A (1–126), B (128–191), C (192–223), D (multicast), E (reserved)

### Subnet Masking
- Divides IP address into Network and Host parts
- CIDR notation: 192.168.1.0/24 → subnet mask 255.255.255.0

### IPv6
- 128-bit address, hexadecimal notation
- Solves IPv4 address exhaustion (4.3 billion limit)
""",
            },
            {
                'title': 'Routing, Switching and Network Security',
                'summary': 'Routing algorithms, switching techniques, network topologies, and security fundamentals.',
                'difficulty': 'hard', 'estimated_minutes': 45,
                'content': """## Network Topologies

| Topology | Description | Advantages | Disadvantages |
|----------|-------------|-----------|---------------|
| **Bus** | Single cable backbone | Easy setup | Single point of failure |
| **Star** | All devices connect to central hub/switch | Easy to manage | Hub failure = network down |
| **Ring** | Devices in a circular chain | Equal access | Single break = failure |
| **Mesh** | Every device connected to every other | Highly reliable | Expensive |
| **Tree** | Hierarchical star topology | Scalable | Root failure = disaster |

## Switching Techniques

| Type | Description |
|------|-------------|
| **Circuit Switching** | Dedicated path established before communication (PSTN phones) |
| **Packet Switching** | Data divided into packets; each routed independently (Internet) |
| **Message Switching** | Store-and-forward; whole message stored at each node |

## Routing

**Routing** — determining the best path for packets from source to destination.

### Static vs Dynamic Routing
- **Static** — manually configured routes; doesn't adapt to changes
- **Dynamic** — automatically updates routes using routing protocols

### Routing Algorithms
| Algorithm | Type | Metric |
|-----------|------|--------|
| **RIP** (Routing Information Protocol) | Distance Vector | Hop count (max 15) |
| **OSPF** (Open Shortest Path First) | Link State | Cost (bandwidth-based) |
| **BGP** (Border Gateway Protocol) | Path Vector | Policy-based; used between ISPs |

### Distance Vector vs Link State
| Feature | Distance Vector | Link State |
|---------|----------------|-----------|
| Knowledge | Knows only neighbours | Full network topology |
| Algorithm | Bellman-Ford | Dijkstra's |
| Convergence | Slow | Fast |
| Bandwidth usage | Low | High |

## Network Security

### Types of Attacks
- **Passive:** Eavesdropping, traffic analysis (doesn't alter data)
- **Active:** Modification, replay attacks, DoS/DDoS (alters data)
- **DoS:** Floods server with requests making it unavailable
- **Man-in-the-Middle (MITM):** Intercepts communication between two parties
- **Phishing:** Fraudulent messages to steal credentials

### Security Mechanisms
| Mechanism | Purpose |
|-----------|---------|
| **Encryption** | Protects data confidentiality |
| **Digital Signatures** | Authentication and non-repudiation |
| **Firewall** | Filters incoming/outgoing network traffic |
| **SSL/TLS** | Secures web communication (HTTPS) |
| **VPN** | Encrypted tunnel over public network |
| **IDS/IPS** | Detects/prevents intrusions |

### Cryptography Basics
- **Symmetric:** Same key for encryption and decryption (AES, DES)
- **Asymmetric:** Public key encrypts, private key decrypts (RSA)
- **Hash Functions:** One-way; verifies integrity (MD5, SHA-256)
""",
            },
        ],
        'questions': [
            {
                'question_text': 'At which OSI layer does the IP protocol operate?',
                'option_a': 'Layer 2 (Data Link)', 'option_b': 'Layer 3 (Network)',
                'option_c': 'Layer 4 (Transport)', 'option_d': 'Layer 7 (Application)',
                'correct_answer': 'B', 'difficulty': 'easy',
                'explanation': 'IP (Internet Protocol) operates at Layer 3 (Network layer) of the OSI model, handling logical addressing and routing.'
            },
            {
                'question_text': 'Which protocol is connection-oriented and provides reliable data delivery?',
                'option_a': 'UDP', 'option_b': 'IP', 'option_c': 'ICMP', 'option_d': 'TCP',
                'correct_answer': 'D', 'difficulty': 'easy',
                'explanation': 'TCP (Transmission Control Protocol) is connection-oriented and provides guaranteed, ordered delivery using acknowledgements and retransmission.'
            },
            {
                'question_text': 'OSPF uses which routing algorithm?',
                'option_a': 'Bellman-Ford', 'option_b': 'Floyd-Warshall', 'option_c': 'Dijkstra\'s', 'option_d': 'Prim\'s',
                'correct_answer': 'C', 'difficulty': 'medium',
                'explanation': 'OSPF (Open Shortest Path First) is a link-state routing protocol that uses Dijkstra\'s algorithm to compute the shortest path tree.'
            },
            {
                'question_text': 'Which port does HTTPS use?',
                'option_a': '80', 'option_b': '22', 'option_c': '443', 'option_d': '25',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'HTTPS (HTTP Secure) uses port 443. HTTP uses port 80, SSH uses 22, and SMTP uses 25.'
            },
        ]
    },

    # ── Unit 9: Software Engineering ────────────────────
    {
        'name': 'Software Engineering',
        'icon': '🔧', 'color': '#4c1d95',
        'description': 'SDLC models, software metrics, testing, project management and quality assurance',
        'topics': [
            {
                'title': 'SDLC Models and Requirements Engineering',
                'summary': 'Software development life cycle models, requirements gathering and software design principles.',
                'difficulty': 'medium', 'estimated_minutes': 45,
                'content': """## Software Development Life Cycle (SDLC)

SDLC is a structured process for developing software systematically.

### Phases of SDLC
1. **Requirements Analysis** — What should the system do?
2. **System Design** — How will the system do it?
3. **Implementation (Coding)** — Build it
4. **Testing** — Does it work correctly?
5. **Deployment** — Release to users
6. **Maintenance** — Fix bugs, add features

## SDLC Models

### 1. Waterfall Model
Sequential, rigid model:
```
Requirements → Design → Implementation → Testing → Deployment → Maintenance
```
- ✅ Simple, easy to manage
- ❌ No going back to previous phase; not suitable for changing requirements

### 2. Prototype Model
Build a prototype, get feedback, refine:
- ✅ User gets to see the system early
- ❌ May lead to "quick and dirty" systems

### 3. Incremental Model
Develop in multiple releases:
- ✅ Working software early; easier to manage
- ❌ More planning overhead

### 4. Spiral Model (Boehm)
Risk-driven model combining iterative development with Waterfall:
**Four phases per spiral:** Planning → Risk Analysis → Engineering → Evaluation
- ✅ Risk analysis at each cycle; suitable for large, complex systems
- ❌ Complex, expensive

### 5. Agile Model
Iterative, incremental, flexible — responds to change.

**Key Agile Frameworks:**
| Framework | Description |
|-----------|-------------|
| **Scrum** | Sprints (1–4 weeks); Product Backlog; Daily Standup |
| **Kanban** | Visual board; WIP limits |
| **XP (Extreme Programming)** | TDD, pair programming, continuous integration |

**Agile Manifesto Values:**
- Individuals over processes
- Working software over comprehensive documentation
- Customer collaboration over contract negotiation
- Responding to change over following a plan

## Requirements Engineering

### Types of Requirements
- **Functional** — what the system should do (features, functions)
- **Non-functional** — quality constraints (performance, security, reliability)

### Requirements Specification
- **SRS (Software Requirements Specification)** — formal document
- **Use Cases** — describe interactions between users and system
- **User Stories** (Agile) — "As a [user], I want [goal] so that [reason]"

## Software Design

### Design Principles
- **Modularity** — break into independent modules
- **Cohesion** — how closely elements within a module are related (higher is better)
- **Coupling** — dependency between modules (lower is better)
- **Abstraction** — hide implementation details

### Design Patterns (GoF)
| Category | Examples |
|----------|---------|
| Creational | Singleton, Factory, Abstract Factory |
| Structural | Adapter, Decorator, Facade |
| Behavioral | Observer, Strategy, Command |
""",
            },
            {
                'title': 'Software Testing and Metrics',
                'summary': 'Testing types, test design techniques, software metrics and quality assurance.',
                'difficulty': 'medium', 'estimated_minutes': 40,
                'content': """## Software Testing

**Goal:** Find defects before release; validate that software meets requirements.

### Testing Levels

| Level | What is Tested | Who Tests |
|-------|---------------|-----------|
| **Unit Testing** | Individual functions/modules | Developers |
| **Integration Testing** | Interaction between modules | Dev/QA |
| **System Testing** | Complete system | QA Team |
| **Acceptance Testing** | Meets user requirements | End Users/Client |

### Testing Approaches

**1. Black-Box Testing (Functional)**
- Tester has **no knowledge** of internal code
- Tests based on requirements/specifications
- Techniques: Equivalence Partitioning, Boundary Value Analysis

**2. White-Box Testing (Structural)**
- Tester has **full knowledge** of source code
- Tests internal logic, code paths
- Techniques: Statement coverage, Branch coverage, Path coverage

**3. Grey-Box Testing**
- Partial knowledge of internals

### Testing Types

| Type | Purpose |
|------|---------|
| **Regression Testing** | Ensure new changes didn't break existing functionality |
| **Performance Testing** | Speed, load, stress testing |
| **Security Testing** | Vulnerabilities, penetration testing |
| **Usability Testing** | User-friendliness |
| **Alpha Testing** | In-house testing before release |
| **Beta Testing** | Selected external users test before full release |

### Test Design Techniques
- **Equivalence Partitioning** — divide input into classes; test one from each
- **Boundary Value Analysis** — test at and around boundaries (0, 1, max, max-1)
- **Decision Table Testing** — test all combinations of conditions

## Software Metrics

### Project Metrics
| Metric | Formula |
|--------|---------|
| **LOC (Lines of Code)** | Physical measure of size |
| **Function Point (FP)** | Measure based on functionality |
| **Cyclomatic Complexity (CC)** | CC = E − N + 2P (E=edges, N=nodes, P=connected components) |

**Cyclomatic Complexity:**
- Measures code complexity
- = Number of linearly independent paths through code
- CC = 1 → simple, sequential
- CC > 10 → complex, hard to test

### Quality Metrics
- **Defect Density** = Defects / KLOC
- **Mean Time to Failure (MTTF)** — reliability measure
- **Mean Time to Repair (MTTR)** — maintainability measure

## Software Project Management

### Cost Estimation Models
- **COCOMO (Constructive Cost Model)** by Boehm
  - Basic, Intermediate, Detailed levels
  - Effort (person-months) = a × (KLOC)^b

### Gantt Charts vs PERT/CPM
- **Gantt Chart** — horizontal bars showing task durations
- **PERT** — probabilistic time estimates; identifies critical path
- **CPM** — deterministic; finds critical path to minimise project duration
""",
            },
        ],
        'questions': [
            {
                'question_text': 'Which SDLC model is most appropriate for projects with high risk and uncertain requirements?',
                'option_a': 'Waterfall', 'option_b': 'Spiral', 'option_c': 'Prototype', 'option_d': 'Incremental',
                'correct_answer': 'B', 'difficulty': 'medium',
                'explanation': 'The Spiral model incorporates risk analysis at each iteration, making it ideal for large, complex, high-risk projects.'
            },
            {
                'question_text': 'Black-box testing is also known as:',
                'option_a': 'Structural testing', 'option_b': 'White-box testing',
                'option_c': 'Functional testing', 'option_d': 'Unit testing',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'Black-box testing (also called functional testing) tests software based on its requirements without knowledge of internal code.'
            },
            {
                'question_text': 'Cyclomatic Complexity measures:',
                'option_a': 'Lines of code', 'option_b': 'Number of test cases',
                'option_c': 'Number of linearly independent paths through code', 'option_d': 'Function points',
                'correct_answer': 'C', 'difficulty': 'medium',
                'explanation': 'Cyclomatic Complexity = E - N + 2P, measuring the number of linearly independent paths (code complexity) in a module.'
            },
            {
                'question_text': 'In Scrum, a fixed-length iteration is called a:',
                'option_a': 'Sprint', 'option_b': 'Milestone', 'option_c': 'Phase', 'option_d': 'Module',
                'correct_answer': 'A', 'difficulty': 'easy',
                'explanation': 'In Scrum, a Sprint is a fixed-length iteration (typically 1–4 weeks) at the end of which a potentially shippable product increment is delivered.'
            },
        ]
    },

    # ── Unit 10: Web Technologies ────────────────────────
    {
        'name': 'Web Technologies',
        'icon': '🕸️', 'color': '#701a75',
        'description': 'HTML, CSS, JavaScript, web architecture, XML, web services, and modern frameworks',
        'topics': [
            {
                'title': 'HTML, CSS and JavaScript Fundamentals',
                'summary': 'Structure (HTML), style (CSS), and behaviour (JavaScript) of web pages.',
                'difficulty': 'easy', 'estimated_minutes': 40,
                'content': """## The Web Technology Stack

| Technology | Role | Type |
|-----------|------|------|
| **HTML** | Structure | Markup |
| **CSS** | Presentation | Stylesheet |
| **JavaScript** | Behaviour | Programming |

## HTML (HyperText Markup Language)

### Document Structure
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Page Title</title>
    <meta charset="UTF-8">
  </head>
  <body>
    <h1>Heading</h1>
    <p>Paragraph</p>
    <a href="https://example.com">Link</a>
    <img src="image.jpg" alt="Description">
  </body>
</html>
```

### Key HTML Elements
| Element | Purpose |
|---------|---------|
| `<h1>–<h6>` | Headings |
| `<p>` | Paragraph |
| `<a href>` | Hyperlink |
| `<img src alt>` | Image |
| `<table>, <tr>, <td>` | Table |
| `<form>, <input>` | Form |
| `<div>` | Block container |
| `<span>` | Inline container |

## CSS (Cascading Style Sheets)

### CSS Selectors
```css
/* Element selector */
p { color: blue; }

/* Class selector */
.highlight { background: yellow; }

/* ID selector */
#header { font-size: 24px; }

/* Descendant selector */
div p { margin: 10px; }
```

### CSS Box Model
```
Margin → Border → Padding → Content
```

### CSS Properties
- **Layout:** `display`, `position`, `float`, `flexbox`, `grid`
- **Typography:** `font-family`, `font-size`, `font-weight`, `line-height`
- **Colors:** `color`, `background-color`

## JavaScript

### Core Concepts
```javascript
// Variables
let x = 10;           // block-scoped, reassignable
const PI = 3.14;      // block-scoped, constant
var name = "Alice";   // function-scoped (avoid)

// Functions
function add(a, b) { return a + b; }
const add = (a, b) => a + b;  // Arrow function

// DOM Manipulation
document.getElementById("myDiv").innerHTML = "Hello!";
document.querySelector(".btn").addEventListener("click", () => {
    alert("Clicked!");
});
```

### JavaScript Events
Common DOM events: `click`, `submit`, `keydown`, `mouseover`, `load`

### JSON (JavaScript Object Notation)
Lightweight data interchange format:
```json
{
    "name": "Alice",
    "age": 22,
    "courses": ["CS", "Math"]
}
```
""",
            },
            {
                'title': 'Web Architecture, XML and Web Services',
                'summary': 'Client-server model, HTTP, XML, REST vs SOAP web services, and modern web frameworks.',
                'difficulty': 'medium', 'estimated_minutes': 45,
                'content': """## Web Architecture

### Client-Server Model
- **Client** — browser (Chrome, Firefox) sends HTTP requests
- **Server** — web server (Apache, Nginx) processes requests and sends responses

### HTTP (HyperText Transfer Protocol)

**HTTP Methods:**
| Method | Purpose |
|--------|---------|
| **GET** | Retrieve data |
| **POST** | Submit data to server |
| **PUT** | Update existing resource |
| **DELETE** | Delete resource |
| **PATCH** | Partial update |

**HTTP Status Codes:**
| Code | Meaning |
|------|---------|
| 200 | OK |
| 201 | Created |
| 301 | Moved Permanently |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

### HTTP vs HTTPS
- **HTTP** — data transmitted in plain text
- **HTTPS** — HTTP + TLS/SSL encryption; uses port 443

## XML (eXtensible Markup Language)

Used for **structured data storage and exchange**.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<students>
    <student id="1">
        <name>Alice</name>
        <gpa>9.5</gpa>
    </student>
</students>
```

### XML vs HTML
| Feature | XML | HTML |
|---------|-----|------|
| Purpose | Data storage/transfer | Display content |
| Tags | Custom, user-defined | Predefined |
| Case sensitive | Yes | No |
| Closing tags | Mandatory | Optional |

### DTD and XML Schema
- **DTD** (Document Type Definition) — defines structure of XML
- **XML Schema (XSD)** — richer, more powerful than DTD

## Web Services

Software services accessible over the web using standard protocols.

### SOAP Web Services
- **Simple Object Access Protocol**
- Uses XML for messaging
- Protocol independent (HTTP, SMTP)
- Heavier, more formal, with WSDL for description

### REST (Representational State Transfer)
- **Architectural style**, not a protocol
- Uses HTTP methods (GET/POST/PUT/DELETE)
- Data in JSON/XML
- Stateless, lightweight, scalable
- Widely used for APIs (Twitter, Google, GitHub)

### REST vs SOAP
| Feature | REST | SOAP |
|---------|------|------|
| Format | JSON, XML | XML only |
| Protocol | HTTP | Any |
| Complexity | Simple | Complex |
| Speed | Faster | Slower |
| Usage | Web APIs | Enterprise |

## Modern Web Technologies

### Frontend Frameworks
- **React.js** — component-based UI (Facebook)
- **Angular** — full MVC framework (Google)
- **Vue.js** — progressive framework

### Backend Frameworks
- **Node.js + Express** — JavaScript server-side
- **Django** — Python
- **Flask** — lightweight Python
- **Spring Boot** — Java

### Databases for Web
- **Relational:** MySQL, PostgreSQL
- **NoSQL:** MongoDB, Redis, Firebase
""",
            },
        ],
        'questions': [
            {
                'question_text': 'Which HTML element is used to create a hyperlink?',
                'option_a': '<link>', 'option_b': '<href>', 'option_c': '<a>', 'option_d': '<url>',
                'correct_answer': 'C', 'difficulty': 'easy',
                'explanation': 'The <a> (anchor) tag with the href attribute creates hyperlinks in HTML: <a href="url">text</a>.'
            },
            {
                'question_text': 'Which HTTP method is used to retrieve data from a server?',
                'option_a': 'POST', 'option_b': 'PUT', 'option_c': 'DELETE', 'option_d': 'GET',
                'correct_answer': 'D', 'difficulty': 'easy',
                'explanation': 'GET is the HTTP method used to request and retrieve data from a server. It should not modify server state.'
            },
            {
                'question_text': 'REST web services primarily use which data format?',
                'option_a': 'XML only', 'option_b': 'JSON (primarily)', 'option_c': 'HTML', 'option_d': 'CSV',
                'correct_answer': 'B', 'difficulty': 'easy',
                'explanation': 'REST APIs primarily use JSON (JavaScript Object Notation) for data exchange, though they can also use XML. JSON is preferred for its simplicity.'
            },
            {
                'question_text': 'Which HTTP status code indicates that a resource was not found?',
                'option_a': '200', 'option_b': '403', 'option_c': '500', 'option_d': '404',
                'correct_answer': 'D', 'difficulty': 'easy',
                'explanation': 'HTTP 404 means "Not Found" — the server could not find the requested resource.'
            },
            {
                'question_text': 'The CSS Box Model from outer to inner is:',
                'option_a': 'Content → Padding → Border → Margin', 'option_b': 'Margin → Border → Padding → Content',
                'option_c': 'Border → Margin → Content → Padding', 'option_d': 'Padding → Content → Margin → Border',
                'correct_answer': 'B', 'difficulty': 'medium',
                'explanation': 'The CSS Box Model from outer to inner: Margin (outermost) → Border → Padding → Content (innermost).'
            },
        ]
    },

]  # end PAPER2_SUBJECTS

# ══════════════════════════════════════════════════════
#  SEED FUNCTION
# ══════════════════════════════════════════════════════


def seed():
    print("Clearing existing data...")
    Question.objects.all().delete()
    Topic.objects.all().delete()
    Subject.objects.all().delete()

    print("Seeding Paper 1 subjects & topics...")
    all_questions = []

    for order_s, subj_data in enumerate(PAPER1_SUBJECTS):
        subj = Subject.objects.create(
            name=subj_data['name'],
            paper='paper1',
            description=subj_data['description'],
            icon=subj_data['icon'],
            color=subj_data['color'],
            order=order_s
        )
        for order_t, t_data in enumerate(subj_data.get('topics', [])):
            slug = slugify(t_data['title'])
            if Topic.objects.filter(slug=slug).exists():
                slug = slug + f'-{subj.id}'
            topic = Topic.objects.create(
                subject=subj,
                title=t_data['title'],
                slug=slug,
                summary=t_data.get('summary', ''),
                content=t_data.get('content', ''),
                difficulty=t_data.get('difficulty', 'medium'),
                estimated_minutes=t_data.get('estimated_minutes', 30),
                order=order_t
            )
            for q_data in subj_data.get('questions', []):
                all_questions.append((topic.id, 'paper1', q_data))

    print("Seeding Paper 2 subjects & topics...")
    for order_s, subj_data in enumerate(PAPER2_SUBJECTS):
        subj = Subject.objects.create(
            name=subj_data['name'],
            paper='paper2',
            description=subj_data['description'],
            icon=subj_data['icon'],
            color=subj_data['color'],
            order=order_s
        )
        for order_t, t_data in enumerate(subj_data.get('topics', [])):
            slug = slugify(t_data['title'])
            if Topic.objects.filter(slug=slug).exists():
                slug = slug + f'-{subj.id}'
            topic = Topic.objects.create(
                subject=subj,
                title=t_data['title'],
                slug=slug,
                summary=t_data.get('summary', ''),
                content=t_data.get('content', ''),
                difficulty=t_data.get('difficulty', 'medium'),
                estimated_minutes=t_data.get('estimated_minutes', 30),
                order=order_t
            )
            for q_data in subj_data.get('questions', []):
                all_questions.append((topic.id, 'paper2', q_data))

    # Deduplicate questions
    seen = set()
    unique_questions = []
    for (topic_id, paper, q_data) in all_questions:
        key = (topic_id, q_data['question_text'][:60])
        if key not in seen:
            seen.add(key)
            unique_questions.append((topic_id, paper, q_data))

    print(f"Seeding {len(unique_questions)} questions...")
    questions_to_create = []
    for topic_id, paper, q_data in unique_questions:
        questions_to_create.append(Question(
            topic_id=topic_id,
            paper=paper,
            question_text=q_data['question_text'],
            option_a=q_data['option_a'],
            option_b=q_data['option_b'],
            option_c=q_data['option_c'],
            option_d=q_data['option_d'],
            correct_answer=q_data['correct_answer'],
            explanation=q_data.get('explanation', ''),
            difficulty=q_data.get('difficulty', 'medium')
        ))
    Question.objects.bulk_create(questions_to_create, batch_size=500)

    print("\n✅ Seed complete!")
    print(f"   Subjects  : {Subject.objects.count()}")
    print(f"   Topics    : {Topic.objects.count()}")
    print(f"   Questions : {Question.objects.count()}")
    print(f"\n   Paper 1 subjects: {Subject.objects.filter(paper='paper1').count()}")
    print(f"   Paper 1 topics  : {Topic.objects.filter(subject__paper='paper1').count()}")
    print(f"   Paper 2 subjects: {Subject.objects.filter(paper='paper2').count()}")
    print(f"   Paper 2 topics  : {Topic.objects.filter(subject__paper='paper2').count()}")

if __name__ == '__main__':
    seed()
