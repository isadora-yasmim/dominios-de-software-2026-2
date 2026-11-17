# UC-14 Responder avaliação

**Projeto:** Sistema de Gestão de Competências (módulo de Feedback)
**Formato:** completo (Larman, cap. 6) · **Issue:** #48 · **Versão:** 1.0 · **Data:** 17/11/2026
**Responsável:** Isadora Yasmim da Silva
**Prioridade:** Must · **Área:** Ciclo de avaliação formal · [Diagrama](Diagrama_Casos_de_Uso.md#43-ciclo-de-avaliação-formal) · [Modelo e convenções](Casos_de_Uso_Completos.md)

---

## 1. Escopo

Sistema de Feedback e Gestão de Competências.

## 2. Nível

Objetivo do usuário.

## 3. Ator principal

**Avaliador convidado**: o colaborador convidado a responder uma avaliação de um ciclo formal, como gestor, par, membro da equipe, liderado na avaliação ascendente ou o próprio avaliado na autoavaliação (diagrama, seção 2).

## 4. Interessados e interesses

| Interessado | Interesse |
|---|---|
| **Avaliador convidado** | Responder rápido, em até 20 minutos por colega (RNF-014). Saber, antes de enviar, quem verá suas respostas e sua identidade (RF-019), para poder ser sincero sem medo de retaliação: a disposição a ser sincero com o gestor identificado foi de 1,5 em 5 nos questionários (RN-004). Não perder o que já escreveu (RNF-012) |
| **Avaliado** | Ser avaliado com base em fatos e comportamentos observados, e não em traços de personalidade ou opinião (RN-001). Receber resultados que possa usar para se desenvolver, comparando a sua percepção com a dos colegas (RF-033; E01 §14) |
| **Gestor que abriu o ciclo** | Receber as respostas dentro do prazo e saber quem não respondeu, porque hoje a participação no 360° não é garantida (RF-029; E01 §21; dor D6 do AS-IS 1) |
| **RH** | Conseguir consultar a identidade do emissor nas modalidades confidenciais (RN-004; E01 §11). Ter respostas comparáveis entre os avaliados, pelo mesmo questionário (RF-007) |
| **Organização contratante** | Avaliação baseada em critérios objetivos, e não só na percepção do avaliador (dor D6 do AS-IS 2). Cumprir a LGPD: aviso honesto sobre a identificação (art. 6º, VI) e anonimato que não possa ser revertido (art. 12) |

## 5. Pré-condições

1. O Avaliador está autenticado (RF-003).
2. Há um ciclo aberto, planejado no UC-13, com modalidade, questionário, modo de identificação e prazo de resposta definidos (RF-022, RF-024, RF-030).
3. Há um convite pendente para o Avaliador nesse ciclo (RF-025, RF-027).

## 6. Garantia de sucesso (pós-condições)

1. A resposta foi gravada de acordo com o modo de identificação da modalidade (RN-004):
   - **identificado**: com a identidade do Avaliador;
   - **confidencial**: sem a identidade junto ao conteúdo. O vínculo entre Avaliador e resposta fica guardado à parte e só o RH pode consultá-lo, com registro na auditoria (RNF-003);
   - **anônimo**: sem nenhum dado que permita chegar ao Avaliador.
2. O convite foi marcado como respondido em registro separado da resposta, sem dado que ligue os dois (DS-12).
3. O rascunho da resposta foi apagado.
4. A resposta está disponível para a consolidação no encerramento do ciclo (UC-16). O avaliado não vê respostas individuais de modalidades confidenciais ou anônimas, apenas resultados consolidados com o mínimo de respondentes (RN-005).

## 7. Cenário de sucesso principal

1. O Avaliador pede para ver as suas avaliações pendentes.
2. O Sistema lista os convites pendentes, com o avaliado, o ciclo, a modalidade e o prazo de cada um (RF-027).
3. O Avaliador escolhe uma avaliação.
4. O Sistema apresenta os objetivos e as competências do ciclo pelos quais a pessoa é avaliada e o questionário da modalidade, com o tipo de resposta de cada pergunta (RF-022, RF-009). Informa também, em linguagem clara, quem poderá ver as respostas e a identidade do Avaliador, conforme o modo de identificação (RF-019, RN-004).
5. O Avaliador consulta os fatos e os feedbacks registrados sobre o avaliado no período do ciclo, entre os que ele já tem permissão para ver (RF-028; UC14-D01).
6. O Avaliador responde às perguntas com base em fatos e comportamentos observados (RN-001).
7. O Sistema salva as respostas como rascunho enquanto o Avaliador preenche (RNF-012).
8. O Avaliador pede para enviar a avaliação.
9. O Sistema confere as respostas e pede a confirmação do envio, repetindo quem poderá ver as respostas e a identidade do Avaliador (RNF-015, RF-019).
10. O Avaliador confirma o envio.
11. O Sistema grava a resposta de acordo com o modo de identificação, marca o convite como respondido em registro separado e apaga o rascunho (RN-004, RNF-003, DS-12).
12. O Sistema confirma o envio ao Avaliador e retira a avaliação da lista de pendentes.

## 8. Extensões

**\*a. A qualquer momento, o Avaliador interrompe o preenchimento ou a sessão expira.**

1. O Sistema mantém o rascunho salvo (RNF-012). A sessão expira após 1 h sem atividade (RNF-006, DS-05).
2. Quando o Avaliador volta e escolhe a mesma avaliação, o Sistema apresenta as respostas do rascunho, e o cenário continua no passo 5.

**2a. Não há avaliações pendentes para o Avaliador.**

1. O Sistema informa que não há avaliações pendentes.
2. O caso de uso termina.

**3a. O prazo de resposta do convite terminou.**

1. O Sistema informa que o prazo terminou e não permite mais responder.
2. O convite fica registrado como não respondido, para consulta do gestor e do RH, sem nenhuma consequência automática para o Avaliador (RF-029; E01 §21).
3. O caso de uso termina.

**4a. A avaliação é uma autoavaliação.**

1. O Sistema informa que a autoavaliação é identificada (RN-004) e que ela será comparada com a avaliação feita pelos demais avaliadores do ciclo (RF-033).
2. O cenário continua no passo 5, e o Avaliador consulta os próprios fatos e feedbacks do período.

**4b. A modalidade é anônima.**

1. Além do aviso do passo 4, o Sistema informa que, depois do envio, a resposta não poderá ser alterada, porque o sistema não guarda nada que a ligue ao Avaliador (UC14-D02).
2. O cenário continua no passo 5.

**5a. Não há fatos nem feedbacks visíveis para o Avaliador no período.**

1. O Sistema informa que não há registros do período que o Avaliador possa consultar.
2. O cenário continua no passo 6.

**6a. O Avaliador preenche uma pergunta de texto livre.**

1. O Sistema orienta a descrever fatos e comportamentos observáveis e a não incluir dados sensíveis, informações de saúde ou dados de terceiros (RF-018).
2. O cenário continua no passo 6.

**9a. Há resposta obrigatória em branco ou valor fora do tipo de resposta da pergunta.**

1. O Sistema identifica cada pergunta com problema e sugere a correção (RNF-021).
2. O cenário volta ao passo 6.

**9b. Um texto livre contém termo da lista de termos ofensivos ou discriminatórios mantida pelo administrador (Could).**

1. O Sistema destaca o trecho e sugere a revisão, sem bloquear o envio (RNF-024, DS-13).
2. O Avaliador revisa o texto, e o cenário volta ao passo 6, **ou** mantém o texto, e o cenário continua no passo 10.

**10a. O Avaliador não confirma o envio.**

1. O Sistema mantém as respostas no rascunho.
2. O cenário volta ao passo 6.

**11a. O Sistema não consegue concluir o envio.**

1. O Sistema informa que a avaliação não foi enviada, mantém o rascunho e deixa o convite como pendente.
2. O cenário volta ao passo 8.

**12a. Depois do envio, com o ciclo ainda aberto, o Avaliador quer alterar uma resposta de modalidade identificada ou confidencial.**

1. O Avaliador escolhe a avaliação já enviada.
2. O Sistema apresenta a resposta enviada para edição.
3. O cenário continua no passo 6. Ao gravar, o Sistema registra a alteração na trilha de auditoria (RNF-005; UC14-D02).

## 9. Requisitos especiais

| Requisito | Como se aplica a este caso de uso |
|---|---|
| Tempo de resposta | O Avaliador conclui a avaliação de um colega em até 20 minutos (RNF-014) |
| Desempenho no pico | O ciclo concentra as respostas na mesma semana. Mesmo com 500 usuários simultâneos, as metas de tempo de RNF-008 continuam valendo (RNF-009, DS-01, DS-03) |
| Rascunho automático | Nada do que foi preenchido se perde com queda de conexão, sessão expirada ou campo obrigatório em branco (RNF-012). O rascunho fica preso ao convite, cifrado, e é apagado no envio (modelo ER, seção 10) |
| Separação entre convite e resposta | O registro de quem respondeu (RF-029) e o conteúdo da resposta não compartilham dado que permita ligá-los, como o horário exato do envio ou o identificador da sessão (DS-12; especificação suplementar, seção 8.3) |
| Trilha de auditoria sem quebra do anonimato | O envio de uma resposta anônima não gera registro de auditoria que ligue o Avaliador ao conteúdo (UC14-D03). Toda consulta do RH ao vínculo de uma resposta confidencial é registrada (RNF-003, RNF-005) |
| Exibição ao avaliado | Respostas de modalidades confidenciais e anônimas só aparecem consolidadas e com no mínimo 3 respondentes, valor configurável (RN-005) |
| Proteção contra erro | Pedir confirmação antes do envio (RNF-015) e indicar o erro com sugestão de correção (RNF-021) |
| Acessibilidade e responsividade | ABNT NBR 17225:2025 e WCAG 2.2 A e AA (RNF-017 a RNF-023). Uso em computador e celular (RNF-027) |

## 10. Lista de variações de tecnologia e dados

1. Tipos de resposta por pergunta: **escala ordinal**, **valor numérico**, **atingido/não atingido** ou **texto livre** (RF-009; E01 §27).
2. Convites e lembretes de avaliação pendente chegam **dentro do sistema e por e-mail** (RF-026, RF-040, DS-10).
3. Uso por **navegador** em computador ou celular: Chrome, Edge, Firefox e Safari, na versão atual e na anterior (RNF-030, DS-07).

## 11. Frequência de ocorrência

Uma vez por convite em cada ciclo formal. A PO citou ciclos de 3 ou 4 meses (E01 §5). Em uma avaliação de equipe, cada membro avalia todos os outros e a si mesmo (E01 §14), o que dá, por ciclo, um número de respostas por avaliador igual ao tamanho da equipe. As respostas se concentram no período de resposta do ciclo (RNF-009).

## 12. Decisões de especificação

| # | Questão | Decisão | Justificativa |
|---|---|---|---|
| UC14-D01 | Quais fatos e feedbacks o Avaliador pode consultar no passo 5? | Só os que ele já tem permissão para ver pelas regras de visibilidade: os que ele mesmo registrou e, se for o gestor direto do avaliado, os que o avaliado recebeu | RF-028 manda respeitar as regras de visibilidade. Pela RNF-001, um feedback só é visto pelo receptor, pelo emissor, pelo gestor direto e pelo RH, e um fato só é visto por quem o registrou até ser vinculado a um feedback (RF-011). Ser convidado para avaliar não amplia esse acesso (RNF-002) |
| UC14-D02 | O Avaliador pode alterar a resposta depois de enviá-la? | Sim, enquanto o ciclo estiver aberto, nos modos identificado e confidencial, com registro na auditoria. No modo anônimo, não, e o Avaliador é avisado antes de responder | No modo anônimo o sistema não sabe qual resposta é de quem, e no confidencial a edição é possível pelo vínculo (modelo ER, seção 10). O limite do encerramento segue a decisão M-08: o resultado consolidado no encerramento não muda depois |
| UC14-D03 | Como registrar o envio de uma resposta anônima na trilha de auditoria? | A trilha registra a mudança do convite para "respondido", mas não registra quem gravou o conteúdo da resposta | A RNF-005 pede trilha dos acessos e alterações a dados pessoais. A resposta anônima não é dado pessoal (LGPD, art. 12), e um registro de quem a gravou recriaria o vínculo que RN-004 e DS-12 proíbem |

## 13. Rastreabilidade

| Tipo | Itens |
|---|---|
| Requisitos funcionais | RF-019, RF-027, RF-028 (do diagrama); RF-009, RF-018, RF-022, RF-029, RF-030, RF-033 (relacionados) |
| Requisitos não funcionais | RNF-001, RNF-002, RNF-003, RNF-005, RNF-006, RNF-008, RNF-009, RNF-012, RNF-014, RNF-015, RNF-017 a RNF-023, RNF-024, RNF-027 |
| Regras de negócio | RN-001, RN-004, RN-005 |
| Entidades do modelo ER | `ConviteAvaliacao`, `RespostaAvaliacao`, `ItemResposta`, `VinculoConfidencial`, `ModalidadeCiclo`, `Pergunta`, `Fato`, `Feedback`, `RegistroAuditoria` |
| Casos de uso relacionados | UC-13 (planejamento do ciclo, pré-condição), UC-15 (acompanhamento de quem não respondeu), UC-16 (consolidação), UC-17 (moderação de resposta inadequada), UC-31 (lembretes de avaliação pendente) |
| Decisões aplicadas | P-01, P-03 (lista geral); DS-01, DS-03, DS-05, DS-07, DS-10, DS-12, DS-13 (especificação suplementar); M-04, M-08 (modelo ER) |
| Fontes | [Entrevista 01](../../elicitacao/entrevistas/Entrevista01_Adriana.md), §5, §11, §14, §21 e §27; [Síntese dos questionários](../../elicitacao/questionarios/Sintese.md); [Processo AS-IS e dores](../../elicitacao/bpmn/Processo_AS-IS_e_Dores.md) |
