# Sistema Web de Feedback e Gestão de Competências

Projeto da disciplina **Domínios de Software (2026/2)** · 1ª Etapa: Levantamento de Requisitos

**Kanban:** [Kanban Domínios de Software](https://github.com/users/isadora-yasmim/projects/3) · **Entrega:** 10/11/2026

---

## Objetivo

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

**15Five** – plataforma de feedback contínuo, avaliação 360° e desenvolvimento. Descrição em [`docs/elicitacao/sistema-analogo/Sistema_Analogo_15Five.md`](docs/elicitacao/sistema-analogo/Sistema_Analogo_15Five.md).

---

## 👥 Integrantes

| Nome | Papel no processo de requisitos | Contato |
|------|-------------------|---------|
| Ana Luísa Pereira dos Santos | Analista de Elicitação | ana_luisa23@discente.ufg.br |
| Davi Augusto Ferreira de Carvalho | Modelador de Sistemas | davi.augusto@discente.ufg.br |
| Isadora Yasmim da Silva | Gerente de Projeto | isadora23456@discente.ufg.br |
| Júlia de Souza Nascimento | Analista de Requisitos Líder | julianascimento@discente.ufg.br |
| Verônica Ribeiro Oliveira Palmeira | Analista de Qualidade e Documentação | veronica_palmeira@discente.ufg.br |

Os papéis estão definidos na seção 4 do [processo de requisitos](docs/Processo_Requisitos.md). A Product Owner (PO) é a Profa. Adriana Silveira de Souza.

---

## Índice dos artefatos

A coluna **Item do enunciado** segue a lista de entregas da 1ª etapa. A conferência completa de cada item está na [revisão final](docs/Revisao_Final.md).

| # | Artefato | Item do enunciado | Local | Issue |
|---|----------|-------------------|-------|-------|
| **Planejamento** |||||
| 1 | Planejamento das atividades (Kanban) | Planejamento das atividades – estilo Kanban | [Project](https://github.com/users/isadora-yasmim/projects/3) | #30 |
| 2 | Definição do processo de requisitos | Definição do processo de requisitos | [`docs/Processo_Requisitos.md`](docs/Processo_Requisitos.md) | #31 |
| **Elicitação** |||||
| 3 | Pesquisa documental (LGPD, ISO/IEC 25010, normas trabalhistas e acessibilidade) | Busca de documentos (leis, regulamentações, padrões 25010) | [`docs/elicitacao/pesquisa-documental/`](docs/elicitacao/pesquisa-documental/) | #33 |
| 4 | Roteiro, termo de consentimento e entrevistas transcritas (2) | Entrega da entrevista transcrita | [`docs/elicitacao/entrevistas/`](docs/elicitacao/entrevistas/) | #34, #35, #36 |
| 5 | Questionários preenchidos (2) | Entrega do questionário preenchido | [`docs/elicitacao/questionarios/`](docs/elicitacao/questionarios/) | #37, #38, #39 |
| 6 | Descrição do sistema análogo (15Five) | Sistemas análogos: funcionalidades descritas | [`docs/elicitacao/sistema-analogo/Sistema_Analogo_15Five.md`](docs/elicitacao/sistema-analogo/Sistema_Analogo_15Five.md) | #32, #40 |
| 7 | Processo de negócio em BPMN (AS-IS e dores) | Processo de negócio de avaliação (principais dores) em BPMN | [`docs/elicitacao/bpmn/`](docs/elicitacao/bpmn/) | #44 |
| **Análise** |||||
| 8 | Síntese dos requisitos das entrevistas | Síntese dos Requisitos das Entrevistas | [`Sintese_Requisitos_Entrevistas.md`](docs/elicitacao/entrevistas/Sintese_Requisitos_Entrevistas.md) | #41 |
| 9 | Síntese dos requisitos dos questionários | Síntese dos Requisitos dos Questionários | [`Sintese.md`](docs/elicitacao/questionarios/Sintese.md) | #42 |
| 10 | Síntese dos requisitos do sistema análogo | Síntese dos Requisitos do Sistema análogo | [`Sintese_Requisitos_Sistema_Analogo.md`](docs/elicitacao/sistema-analogo/Sintese_Requisitos_Sistema_Analogo.md) | #43 |
| 11 | Lista de requisitos — geral | Lista de requisitos – Geral | [`docs/Lista_Geral_Requisitos.md`](docs/Lista_Geral_Requisitos.md) · [CSV](docs/Lista_Geral_Requisitos.csv) | #45 |
| 12 | Matriz de rastreabilidade (horizontal e vertical) | Matriz de Rastreabilidade (horizontal e vertical) | [`docs/Matriz_Rastreabilidade.md`](docs/Matriz_Rastreabilidade.md) · [CSV](docs/Matriz_Rastreabilidade.csv) | #49 |
| **Especificação** |||||
| 13 | Documento Visão (Larman, cap. 7) | Documento Visão – cap. 7 | [`docs/Documento_Visao.md`](docs/Documento_Visao.md) | #46 |
| 14 | Especificação suplementar: RNF segundo ISO/IEC 25010 (Larman, cap. 7) | Especificação suplementar (ISO/IEC 25010) – cap. 7 | [`docs/Especificacao_Suplementar.md`](docs/Especificacao_Suplementar.md) | #51 |
| 15 | Dicionário de dados e glossário (Larman, cap. 7) | Dicionário de dados (glossário) – cap. 7 | [`docs/Dicionario_de_Dados.md`](docs/Dicionario_de_Dados.md) | #53 |
| 16 | Especificação de requisitos (IEEE 830) | Especificação de Requisitos – IEEE 830 e/ou EOR | [`docs/Especificacao_Requisitos_IEEE830.md`](docs/Especificacao_Requisitos_IEEE830.md) | #54 |
| **Modelagem** |||||
| 17 | Diagrama de casos de uso (Larman, cap. 6) | Diagrama de casos de uso – cap. 6 | [`Diagrama_Casos_de_Uso.md`](docs/modelagem/casos-de-uso/Diagrama_Casos_de_Uso.md) | #47 |
| 18 | Casos de uso completos, 1 por integrante (Larman, cap. 6) | Casos de uso essenciais, 1 completo por integrante – cap. 6 | [`Casos_de_Uso_Completos.md`](docs/modelagem/casos-de-uso/Casos_de_Uso_Completos.md) | #48 |
| 19 | Modelo de domínio e entidade-relacionamento | Modelo Entidade Relacionamento / Modelo de domínio | [`Modelo_Dominio_ER.md`](docs/modelagem/modelo-dados/Modelo_Dominio_ER.md) | #52 |
| **Protótipos** |||||
| 20 | Protótipos das telas (Figma) | Protótipos das telas – Figma | [`docs/prototipacao/Prototipo.md`](docs/prototipacao/Prototipo.md) · [abrir no Figma](https://www.figma.com/design/yiyjqLFpIp838MAi9x0EW4/Dom%C3%ADnios-de-Software-2026-2?node-id=6-3) | #50 |
| **Entrega** |||||
| 21 | Revisão final e consolidação | Todos os artefatos armazenados em controle de versões | [`docs/Revisao_Final.md`](docs/Revisao_Final.md) | #55 |
| 22 | Apresentação final | Entrega e apresentação do trabalho | — | #56 |

---

## Estrutura do repositório

```
docs/
├── Processo_Requisitos.md
├── Lista_Geral_Requisitos.md / .csv
├── Matriz_Rastreabilidade.md / .csv
├── Documento_Visao.md
├── Especificacao_Suplementar.md
├── Dicionario_de_Dados.md
├── Especificacao_Requisitos_IEEE830.md
├── Revisao_Final.md
├── assets/
├── elicitacao/
│   ├── bpmn/
│   ├── entrevistas/
│   ├── pesquisa-documental/
│   ├── questionarios/
│   └── sistema-analogo/
├── modelagem/
│   ├── casos-de-uso/
│   └── modelo-dados/
└── prototipacao/
```

## Convenções

- **Identificação de requisitos:** `RF-001` (funcional), `RNF-001` (não funcional), `RN-001` (regra de negócio), `UC-01` (caso de uso).
- **Branches:** uma branch curta por issue, no formato `<nº-da-issue>-<descricao-curta>`, por exemplo `6-entrevista-1`. A branch sai sempre da `main` atualizada e é apagada depois do merge.
- **Pull Requests:** todo trabalho entra na `main` por PR, com pelo menos 1 aprovação de outro integrante. Na descrição do PR, use `Closes #<nº>` para a issue fechar e o card andar no Kanban sozinho.
- **Commits:** referenciem a issue, por exemplo `docs: transcrição da entrevista 1 (#6)`.
- **Arquivos binários** (.docx, .pdf, imagens): cada arquivo tem um único responsável por vez, porque o Git não mescla esses formatos. Prefira Markdown sempre que possível.
- **LGPD:** dados de entrevistados e respondentes (nome, função, telefone) só entram no repositório com consentimento registrado. Mantenha o repositório **privado** enquanto houver dados pessoais.

### Fluxo de trabalho

```bash
git checkout main && git pull
git checkout -b 6-entrevista-1
# ... edita os arquivos ...
git add . && git commit -m "docs: transcrição da entrevista 1 (#6)"
git push -u origin 6-entrevista-1
# abra o PR no GitHub com "Closes #6" na descrição
```

## Referências

- LARMAN, C. *Utilizando UML e Padrões*. Caps. 6 e 7.
- ISO/IEC 25010 — Modelo de qualidade de produto de software.
- IEEE 830 — Práticas recomendadas para especificação de requisitos de software.
- Lei nº 13.709/2018 — Lei Geral de Proteção de Dados (LGPD).
