# Sistema de Gestão de Competências — Feedback

Projeto da disciplina **Domínios de Software (2026/2)** · 1ª Etapa: Levantamento de Requisitos

📋 **Kanban:** [Kanban Domínios de Software](https://github.com/users/isadora-yasmim/projects/3) · 🗓️ **Entrega:** 10/11/2026

---

## 🎯 Objetivo

Levantar e especificar os requisitos de um **sistema web de gestão de competências baseado em feedback**. O sistema terá versão futura para dispositivos móveis e deve estar em conformidade com a **LGPD** (Lei nº 13.709/2018).

O sistema deve permitir:

- **Diversas fontes de feedback:** chefe → colaborador, entre pares e avaliação 360º, sempre com base em dados coletados dos emissores.
- **Diferentes tipos de feedback:** formal, informal, positivo e construtivo.
- **Questionários:** perguntas que apoiam os emissores na avaliação e orientam os receptores sobre suas metas e competências.
- **Análise robusta:** indicadores, tendências e gráficos que mostram a evolução de cada colaborador.
- **Confidencialidade e anonimato:** proteção da identidade dos respondentes e das avaliações, para incentivar feedback honesto.
- **Acompanhamento:** planos de ação de melhoria e histórico completo dos feedbacks.
- **Planejamento de desenvolvimento:** definição de metas e acompanhamento das melhorias ao longo do tempo.

### Sistema análogo analisado

> _A definir (issue #3)._

---

## 👥 Integrantes

| Nome | Função no projeto | Contato |
|------|-------------------|---------|
| _Integrante 1_ | | |
| _Integrante 2_ | | |
| _Integrante 3_ | | |
| _Integrante 4_ | | |
| _Integrante 5_ | | |
| _Integrante 6_ | | |
| _Integrante 7_ | | |
| _Integrante 8_ | | |

---

## 📂 Índice dos artefatos

| # | Artefato | Local | Issue |
|---|----------|-------|-------|
| **Planejamento** ||||
| 1 | Planejamento das atividades (Kanban) | [Project](https://github.com/users/isadora-yasmim/projects/3) | #1 |
| 2 | Definição do processo de requisitos | [`docs/01-planejamento/`](docs/01-planejamento/) | #2 |
| **Elicitação** ||||
| 3 | Pesquisa documental (LGPD, ISO/IEC 25010, regulamentações) | [`docs/02-elicitacao/pesquisa-documental/`](docs/02-elicitacao/pesquisa-documental/) | #4 |
| 4 | Roteiro e entrevistas transcritas (2) | [`docs/02-elicitacao/entrevistas/`](docs/02-elicitacao/entrevistas/) | #5 #6 #7 |
| 5 | Questionário e questionários preenchidos (2) | [`docs/02-elicitacao/questionarios/`](docs/02-elicitacao/questionarios/) | #8 #9 #10 |
| 6 | Descrição do sistema análogo | [`docs/02-elicitacao/sistema-analogo/`](docs/02-elicitacao/sistema-analogo/) | #11 |
| 7 | Processo de negócio em BPMN (AS-IS e dores) | [`docs/02-elicitacao/bpmn/`](docs/02-elicitacao/bpmn/) | #15 |
| **Análise** ||||
| 8 | Síntese dos requisitos das entrevistas | [`docs/03-analise/`](docs/03-analise/) | #12 |
| 9 | Síntese dos requisitos dos questionários | [`docs/03-analise/`](docs/03-analise/) | #13 |
| 10 | Síntese dos requisitos do sistema análogo | [`docs/03-analise/`](docs/03-analise/) | #14 |
| 11 | Lista de requisitos — geral | [`docs/03-analise/`](docs/03-analise/) | #16 |
| 12 | Matriz de rastreabilidade (horizontal e vertical) | [`docs/03-analise/`](docs/03-analise/) | #20 |
| **Especificação** ||||
| 13 | Documento Visão (Larman, cap. 7) | [`docs/04-especificacao/`](docs/04-especificacao/) | #17 |
| 14 | Especificação suplementar: RNF segundo ISO/IEC 25010 (Larman, cap. 7) | [`docs/04-especificacao/`](docs/04-especificacao/) | #22 |
| 15 | Dicionário de dados / glossário (Larman, cap. 7) | [`docs/04-especificacao/`](docs/04-especificacao/) | #24 |
| 16 | Especificação de Requisitos (IEEE 830 e/ou EOR) | [`docs/04-especificacao/`](docs/04-especificacao/) | #25 |
| **Modelagem** ||||
| 17 | Diagrama de casos de uso (Larman, cap. 6) | [`docs/05-modelagem/casos-de-uso/`](docs/05-modelagem/casos-de-uso/) | #18 |
| 18 | Casos de uso completos, 1 por integrante (Larman, cap. 6) | [`docs/05-modelagem/casos-de-uso/`](docs/05-modelagem/casos-de-uso/) | #19 |
| 19 | Modelo entidade-relacionamento / modelo de domínio | [`docs/05-modelagem/modelo-dados/`](docs/05-modelagem/modelo-dados/) | #23 |
| **Protótipos** ||||
| 20 | Protótipos das telas (Figma) | [`docs/06-prototipos/`](docs/06-prototipos/) · _link do Figma a definir_ | #21 |
| **Entrega** ||||
| 21 | Apresentação final | [`docs/07-entrega/`](docs/07-entrega/) | #27 |

---

## 🗂️ Estrutura do repositório

```
docs/
├── 01-planejamento/
├── 02-elicitacao/
│   ├── pesquisa-documental/
│   ├── entrevistas/
│   ├── questionarios/
│   ├── sistema-analogo/
│   └── bpmn/
├── 03-analise/
├── 04-especificacao/
├── 05-modelagem/
│   ├── casos-de-uso/
│   └── modelo-dados/
├── 06-prototipos/
└── 07-entrega/
```

## 🔖 Convenções

- **Identificação de requisitos:** `RF-001` (funcional), `RNF-001` (não funcional), `RN-001` (regra de negócio), `UC-01` (caso de uso).
- **Commits:** referenciem a issue, por exemplo `docs: transcrição da entrevista 1 (#6)`.
- **LGPD:** dados de entrevistados e respondentes (nome, função, telefone) só entram no repositório com consentimento registrado. Mantenha o repositório **privado** enquanto houver dados pessoais.

## 📚 Referências

- LARMAN, C. *Utilizando UML e Padrões*. Caps. 6 e 7.
- ISO/IEC 25010 — Modelo de qualidade de produto de software.
- IEEE 830 — Práticas recomendadas para especificação de requisitos de software.
- Lei nº 13.709/2018 — Lei Geral de Proteção de Dados (LGPD).
