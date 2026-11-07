# Sistema de Gestão de Competências — Feedback

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

> _A definir (issue #3)._

---

## 👥 Integrantes

| Nome | Função no projeto | Contato |
|------|-------------------|---------|
| _Integrante 1_ | Ana Luísa Pereira dos Santos| ana_luisa23@discente.ufg.br|
| _Integrante 2_ | Davi Augusto Ferreira de Carvalho| davi.augusto@discente.ufg.br|
| _Integrante 3_ | Isadora Yasmim da Silva| isadora23456@discente.ufg.br|
| _Integrante 4_ | Júlia de Souza Nascimento| julianascimento@discente.ufg.br|
| _Integrante 5_ | Verônica Ribeiro Oliveira Palmeira| veronica_palmeira@discente.ufg.br|


---

## Índice dos artefatos

| # | Artefato | Local | Issue |
|---|----------|-------|-------|
| **Planejamento** ||||
| 1 | Planejamento das atividades (Kanban) | [Project](https://github.com/users/isadora-yasmim/projects/3) | #1 |
| 2 | Definição do processo de requisitos | [`docs/`](docs/) | #2 |
| **Elicitação** ||||
| 3 | Pesquisa documental (LGPD, ISO/IEC 25010, regulamentações) | [`docs/elicitacao/pesquisa-documental/`](docs/elicitacao/pesquisa-documental/) | #4 |
| 4 | Roteiro e entrevistas transcritas (2) | [`docs/elicitacao/entrevistas/`](docs/elicitacao/entrevistas/) | #5 #6 #7 |
| 5 | Questionário e questionários preenchidos (2) | [`docs/elicitacao/questionarios/`](docs/elicitacao/questionarios/) | #8 #9 #10 |
| 6 | Descrição do sistema análogo | [`docs/elicitacao/sistema-analogo/`](docs/elicitacao/sistema-analogo/) | #11 |
| 7 | Processo de negócio em BPMN (AS-IS e dores) | [`docs/elicitacao/bpmn/`](docs/elicitacao/bpmn/) | #15 |
| **Análise** ||||
| 8 | Síntese dos requisitos das entrevistas | [`docs/`](docs/) | #12 |
| 9 | Síntese dos requisitos dos questionários | [`docs/`](docs/) | #13 |
| 10 | Síntese dos requisitos do sistema análogo | [`docs/`](docs/) | #14 |
| 11 | Lista de requisitos — geral | [`docs/`](docs/) | #16 |
| 12 | Matriz de rastreabilidade (horizontal e vertical) | [`docs/`](docs/) | #20 |
| **Especificação** ||||
| 13 | Documento Visão (Larman, cap. 7) | [`docs/`](docs/) | #17 |
| 14 | Especificação suplementar: RNF segundo ISO/IEC 25010 (Larman, cap. 7) | [`docs/`](docs/) | #22 |
| 15 | Dicionário de dados / glossário (Larman, cap. 7) | [`docs/`](docs/) | #24 |
| 16 | Especificação de Requisitos (IEEE 830 e/ou EOR) | [`docs/`](docs/) | #25 |
| **Modelagem** ||||
| 17 | Diagrama de casos de uso (Larman, cap. 6) | [`docs/modelagem/casos-de-uso/`](docs/modelagem/casos-de-uso/) | #18 |
| 18 | Casos de uso completos, 1 por integrante (Larman, cap. 6) | [`docs/modelagem/casos-de-uso/`](docs/modelagem/casos-de-uso/) | #19 |
| 19 | Modelo entidade-relacionamento / modelo de domínio | [`docs/modelagem/modelo-dados/`](docs/modelagem/modelo-dados/) | #23 |
| **Protótipos** ||||
| 20 | Protótipos das telas (Figma) | [`docs/prototipacao/`](docs/prototipacao/) · _link do Figma a definir_ | #21 |
| **Entrega** ||||
| 21 | Apresentação final | [`docs/`](docs/) | #27 |

---

## Estrutura do repositório

```
docs/
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
