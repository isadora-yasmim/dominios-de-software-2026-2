# Processo AS-IS de feedback e avaliação, com as dores (Issue #44)

Projeto: Sistema Web de Feedback e Gestão de Competências · Disciplina Domínios de Software (INF0296, 2026/2)

## 1. Escopo

Modelagem em BPMN do processo de avaliação e feedback **como acontece hoje**, com raias RH, Gestor, Colaborador e Pares e as principais dores destacadas em vermelho. Foram feitos dois diagramas, numerados como as entrevistas que os originaram.

| Diagrama | Fonte | Contexto | Arquivos |
|---|---|---|---|
| AS-IS 1 | Entrevista 01 | Product Owner da disciplina, falando como usuária e também sobre a prática ideal | `AS-IS_01_Product_Owner.bpmn` / `.png` / `.svg` |
| AS-IS 2 | Entrevista 02 | Secretária Municipal de Educação (cidade pequena, equipe da secretaria) | `AS-IS_02_Secretaria_Educacao.bpmn` / `.png` / `.svg` |

## 2. Notação

- Pool único com 4 raias: RH, Gestor, Colaborador, Pares.
- Círculo fino = início, círculo grosso = fim, losango com X = decisão, losango com + = paralelo.
- **Vermelho** = tarefa ou decisão onde há dor. A anotação vermelha ligada ao elemento traz o código da dor (D1 a D6).
- A legenda abaixo de cada diagrama lista as dores com as seções da entrevista que as sustentam.

## 3. AS-IS 1 (Entrevista 01)

**Feedback formal (ciclo planejado)**: o gestor planeja objetivos, competências e indicadores, depois coleta fatos e faz check-ins. Em paralelo, o colaborador faz a autoavaliação e os pares respondem o 360º. O gestor agenda a sessão e a conduz (positivo ou construtivo). O colaborador recebe e reflete. O gestor registra e avalia a sessão. Se foi construtivo, constrói o plano de ação com o colaborador, monitora, e verifica se melhorou. Se não melhorou, abre nova rodada.

**Feedback informal**: o gestor observa um fato no dia a dia, decide dar o feedback e conduz a sessão.

**RH**: treina quem dá e quem recebe feedback, e consulta o histórico quando há decisão sobre a pessoa (por exemplo, promoção).

| Código | Dor | Onde aparece | Entrevista 01 |
|---|---|---|---|
| D1 | Registro manual (papel, Excel), informação se perde, informal fica só na conversa | Coletar fato, Registrar | seções 6 e 18 |
| D2 | Planejar e acompanhar cada pessoa dá trabalho e falta tempo | Planejar | seção 9 |
| D3 | Reação defensiva, feedback visto como crítica destrutiva | Receber o feedback | seções 13, 20 e 22 |
| D4 | Sem controle se a pessoa melhorou | Verificação final | seção 6 |
| D5 | Feedback mal dado (pouco elogio, crítica agressiva) | Conduzir o feedback | seção 20 |
| D6 | Participação no 360º não garantida | Avaliar o colega | seção 21 |

## 4. AS-IS 2 (Entrevista 02)

A secretária percebe um problema ou recebe a queixa de um colega (que fica anônimo). Ela confirma o fato por conta própria e anota no caderninho, nem sempre. Se há horário em comum, chama a pessoa no particular no fim do expediente. Caso contrário, o feedback passa batido. A pessoa ouve e responde. Se discorda, justifica e a conversa vira discussão. Depois, combina a melhoria de forma verbal e acompanha de modo informal. O elogio, quando acontece, vai por mensagem de WhatsApp. Não há registro formal.

A raia do RH fica sem tarefas, de propósito: a secretária responde ao prefeito e o RH não participa. O estágio probatório segue a regra do órgão responsável e ficou fora do fluxo (anotações cinzas).

| Código | Dor | Onde aparece | Entrevista 02 |
|---|---|---|---|
| D1 | Sem registro, tudo de boca | Anotar no caderninho | seções 2, 3 e 4 |
| D2 | Agendas não coincidem, feedback passa batido | Há horário em comum? | seções 2 e 8 |
| D3 | Pessoa se justifica e vira discussão | Justificar e discordar | seção 2 |
| D4 | Acompanhamento depende da memória | Acompanhar | seção 4 |
| D5 | Anonimato só pela discrição da secretária | Avisar a secretária | seções 3 e 6 |
| D6 | Sem formulário nem indicadores | Confirmar o fato | seção 5 |

## 5. Comparação rápida

- Registro (D1) e acompanhamento sem controle (D4) aparecem nos dois casos, então são fortes candidatos a requisitos centrais (histórico de feedbacks, plano de ação com prazo e lembretes).
- Dificuldade de agenda e de tempo (D2) e reação defensiva (D3) também são comuns.
- A PO descreve um processo estruturado, mas manual. A secretaria tem um processo totalmente informal.
- Anonimato (D5 da Secretaria) e participação no 360º (D6 da PO) sugerem requisitos de avaliação anônima e lembretes.

## 6. Como abrir e editar

Os arquivos `.bpmn` são texto (Git friendly). Abra em [demo.bpmn.io](https://demo.bpmn.io) (Open) ou no Camunda Modeler. Os `.png` e `.svg` foram exportados com bpmn-js.

## 7. Observações

- A PO falou também sobre a prática ideal, por isso o Diagrama 1 representa o processo segundo ela.
- O README lista a issue de BPMN como #15, mas o roteiro e a issue são #44. Vale alinhar com o grupo.
- O TO-BE (opcional na issue) não foi feito.
