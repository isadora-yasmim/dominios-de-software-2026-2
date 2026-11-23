# UC-13 Planejar ciclo de avaliação

**Projeto:** Sistema Web de Feedback e Gestão de Competências
**Formato:** completo (Larman, cap. 6) · **Issue:** #48 · **Versão:** 1.0 · **Data:** 17/11/2026
**Responsável:** Júlia de Souza Nascimento
**Prioridade:** Must · **Área:** Ciclo de avaliação formal · [Diagrama](../Diagrama_Casos_de_Uso.md#43-ciclo-de-avaliação-formal) · [Modelo e convenções](../Casos_de_Uso_Completos.md)

---

## 1. Escopo

Sistema Web de Feedback e Gestão de Competências.

## 2. Nível

Objetivo do usuário.

## 3. Ator principal

**Gestor**: o gestor que planeja o feedback formal da sua equipe ou de um colaborador (E01 §5, §17). O **RH** também pode planejar ciclos para qualquer equipe da organização (RF-022) e é o único que altera o modo de identificação padrão das modalidades (RF-030; UC13-D02).

## 4. Interessados e interesses

| Interessado | Interesse |
|---|---|
| **Gestor** | Planejar o ciclo sem retrabalho, reaproveitando questionários e parâmetros de ciclos anteriores (RF-007; E01 §15). Hoje planejar e acompanhar cada pessoa dá trabalho e falta tempo (dor D2 do AS-IS 1). Saber depois quem participou e quem não participou (RF-029; E01 §21) |
| **Avaliado** | Saber desde o início **o que** será avaliado, por quais indicadores e quando serão os check-ins, para saber o que é esperado dele (RF-026; E01 §19, §29). Ser avaliado por critérios objetivos, e não por opinião (RN-001; E01 §29) |
| **Avaliadores convidados** | Ser avisados do convite e do prazo (RF-026, RF-040). Saber, antes de responder, se a sua identidade ficará protegida, o que depende do modo de identificação definido aqui (RN-004) |
| **RH** | Ter ciclos comparáveis entre as equipes, com o questionário padrão da organização (RF-008). Garantir que os modos de identificação sigam RN-004 (RF-030) |
| **Organização contratante** | Avaliação por indicadores, e não só pela percepção do gestor (dor D6 do AS-IS 2). Participação garantida no 360°, que hoje não é (dor D6 do AS-IS 1). Critérios iguais para todos no mesmo cargo, se o histórico for usado em decisões sobre pessoas (RN-007) |

## 5. Pré-condições

1. O Gestor está autenticado com o perfil gestor ou RH (RF-003).
2. A estrutura da organização está cadastrada: colaboradores, cargos, equipes e quem é gestor de quem (UC-01, RF-001).
3. As competências dos cargos estão cadastradas (UC-03, RF-005).
4. Existe pelo menos um questionário de avaliação, por exemplo o padrão da organização (UC-05, RF-007, RF-008).

## 6. Garantia de sucesso (pós-condições)

1. O ciclo foi gravado com período, avaliados, objetivos, indicadores, competências, modalidades, questionário, modo de identificação e peso de cada modalidade, participantes, datas dos check-ins e prazo de resposta (RF-022, RF-023, RF-024, RF-030).
2. Cada modalidade tem um modo de identificação permitido por RN-004, e o mínimo de respondentes da organização foi aplicado às modalidades confidenciais e anônimas (RN-005).
3. O ciclo está **aberto**, e um convite pendente foi criado para cada avaliador em cada modalidade (RF-025, RF-027).
4. Cada avaliado foi notificado sobre os objetivos, as competências, os indicadores e as datas dos check-ins, e cada avaliador foi notificado sobre o convite e o prazo (RF-026; DS-10).
5. Os check-ins foram agendados nas datas definidas (RF-022).

## 7. Cenário de sucesso principal

1. O Gestor pede para planejar um novo ciclo de avaliação.
2. O Sistema pede os dados gerais do ciclo e oferece, como ponto de partida, copiar um ciclo anterior (RF-007; UC13-D01).
3. O Gestor informa o título e o período do ciclo e escolhe os avaliados entre os colaboradores da sua equipe (RF-022).
4. O Gestor define os objetivos do ciclo, cada um de comportamento ou de resultado (RF-022; E01 §5).
5. Para cada objetivo, o Gestor define um ou mais indicadores, com a fonte de evidência e o valor esperado (RF-023; E01 §5, §29).
6. O Sistema apresenta as competências do cargo e as competências específicas de cada avaliado, e o Gestor escolhe as que o ciclo vai avaliar (RF-005, RF-006, RF-022).
7. O Gestor escolhe as modalidades do ciclo, como gestor → colaborador, autoavaliação e pares, e o questionário de cada uma (RF-024, RF-007).
8. O Sistema apresenta, para cada modalidade, o modo de identificação padrão de RN-004 e o mínimo de respondentes da organização (RN-004, RN-005; UC13-D02).
9. O Gestor define os participantes de cada modalidade, entre os membros da sua equipe (RF-025).
10. O Gestor define as datas dos check-ins e o prazo de resposta das avaliações (RF-022).
11. O Sistema confere o planejamento e apresenta um resumo com os avaliados, os objetivos, os indicadores, as modalidades, quem avalia quem, o modo de identificação de cada modalidade e as datas (RNF-015).
12. O Gestor pede para abrir o ciclo.
13. O Sistema pede a confirmação, informando que os avaliados e os avaliadores serão notificados e o que não poderá mais ser alterado depois da abertura (RNF-015; UC13-D03).
14. O Gestor confirma.
15. O Sistema grava o ciclo como aberto, cria os convites de avaliação, agenda os check-ins e notifica cada avaliado sobre o que será avaliado e cada avaliador sobre o convite e o prazo (RF-026, RF-027; DS-10).
16. O Sistema confirma ao Gestor que o ciclo foi aberto e passa a mostrá-lo entre os ciclos em andamento, para acompanhamento no UC-15.

## 8. Extensões

**\*a. A qualquer momento, o Gestor interrompe o planejamento ou a sessão expira.**

1. O Sistema mantém o que já foi preenchido como ciclo **planejado**, ainda não aberto e sem notificar ninguém (RNF-012; UC13-D04).
2. Quando o Gestor volta e escolhe o ciclo planejado, o cenário continua no passo em que parou.

**2a. O Gestor escolhe copiar um ciclo anterior.**

1. O Sistema preenche os objetivos, os indicadores, as competências, as modalidades, os questionários e os modos de identificação do ciclo escolhido, sem os avaliados, os participantes e as datas (UC13-D01).
2. O cenário continua no passo 3, e o Gestor pode ajustar cada item copiado.

**3a. O receptor do ciclo é uma equipe.**

1. O Gestor escolhe a equipe, e o Sistema inclui todos os seus membros como avaliados (RF-022).
2. O cenário continua no passo 4. Na modalidade de equipe, cada membro avalia todos os outros (RF-024; E01 §21).

**3b. O planejador é o RH.**

1. O Sistema permite escolher avaliados de qualquer equipe da organização (RF-022).
2. O cenário continua no passo 4.

**3c. A data final do período é anterior à data inicial ou já passou.**

1. O Sistema indica o erro e sugere a correção (RNF-021).
2. O cenário volta ao passo 3.

**5a. Um objetivo fica sem indicador.**

1. O Sistema avisa que o objetivo não poderá ser medido nos check-ins e pede pelo menos um indicador (RF-023; UC13-D05).
2. O cenário volta ao passo 5.

**6a. Um avaliado ainda não tem competências cadastradas para o seu cargo.**

1. O Sistema informa a falta e permite ao Gestor atribuir competências específicas a esse avaliado (UC-04, RF-006).
2. O cenário continua no passo 6.

**7a. Não há questionário adequado para uma modalidade.**

1. O Gestor parte do questionário padrão da organização e acrescenta perguntas específicas para o avaliado (UC-05, RF-008; E01 §29).
2. O cenário continua no passo 7.

**7b. O Gestor escolhe a modalidade 360°.**

1. O Sistema inclui no ciclo as modalidades gestor → colaborador, pares, avaliação ascendente e autoavaliação, cada uma com seu modo de identificação (RF-024).
2. O cenário continua no passo 8.

**7c. A organização usa pesos (Could).**

1. O Gestor atribui um peso a cada modalidade e a cada indicador para o cálculo do resultado consolidado (RF-010).
2. O Sistema mostra os pesos no resumo do passo 11, para que os critérios do cálculo fiquem visíveis (RN-008).
3. O cenário continua no passo 8.

**8a. O planejador é o RH e quer mudar o modo de identificação de uma modalidade.**

1. O Sistema permite trocar entre **confidencial** e **anônimo** nas modalidades ascendente, pares e equipe. A modalidade gestor → colaborador e a autoavaliação continuam **identificadas** (RF-030, RN-004).
2. Se o RH também for avaliado no ciclo, o Sistema informa que ele não poderá consultar a identidade de quem o avaliar (RN-004).
3. O cenário continua no passo 9.

**8b. O planejador é o Gestor e quer mudar o modo de identificação.**

1. O Sistema informa que só o RH altera o modo padrão e que o Gestor pode pedir a mudança ao RH (RF-030; UC13-D02).
2. O cenário continua no passo 9 com o modo padrão.

**9a. O Gestor tenta convidar alguém que não é da sua equipe para o 360° ou para a avaliação de pares.**

1. O Sistema informa que os participantes precisam ser membros da equipe do gestor que abriu o ciclo (RF-025; E01 §21).
2. O cenário volta ao passo 9.

**9b. Uma modalidade confidencial ou anônima tem menos participantes do que o mínimo de respondentes.**

1. O Sistema avisa que, se o mínimo não for atingido, as respostas dessa modalidade não aparecerão isoladas para o avaliado e serão somadas a outra categoria ou omitidas (RN-005).
2. O Gestor acrescenta participantes, e o cenário volta ao passo 9, **ou** mantém a lista, e o cenário continua no passo 10.

**10a. Uma data de check-in fica fora do período do ciclo, ou o prazo de resposta passa da data final.**

1. O Sistema indica as datas com problema e sugere a correção (RNF-021).
2. O cenário volta ao passo 10.

**12a. O Gestor quer revisar o planejamento antes de abrir.**

1. O Gestor salva o ciclo como **planejado**, sem notificar ninguém (UC13-D04).
2. O caso de uso termina. O Gestor pode retomar o ciclo depois, como em \*a.

**12b. O Gestor quer abrir o ciclo em uma data futura.**

1. O Gestor salva o ciclo como planejado com a data de abertura igual à data inicial do período.
2. Na data inicial, o Sistema abre o ciclo e faz o passo 15 automaticamente (UC-31).
3. O caso de uso termina.

**14a. O Gestor não confirma a abertura.**

1. O Sistema mantém o ciclo como planejado.
2. O cenário volta ao passo 11.

**15a. O Sistema não consegue concluir a abertura.**

1. O Sistema informa que o ciclo não foi aberto, mantém o planejamento gravado como planejado e não envia nenhuma notificação parcial.
2. O cenário volta ao passo 12.

**16a. Depois da abertura, o Gestor precisa alterar o ciclo.**

1. O Gestor escolhe o ciclo aberto.
2. O Sistema permite acrescentar participantes e avaliados, mudar as datas dos check-ins e prorrogar o prazo de resposta. Não permite mudar o questionário nem o modo de identificação das modalidades (UC13-D03).
3. O Sistema notifica as pessoas afetadas pela alteração e registra a alteração na trilha de auditoria (RF-026, RNF-005).

## 9. Requisitos especiais

| Requisito | Como se aplica a este caso de uso |
|---|---|
| Parametrização sem código | Questionários, modalidades e parâmetros do ciclo são definidos pela interface, sem intervenção técnica (RNF-026) |
| Modos de identificação | Cada modalidade só aceita os modos permitidos por RN-004. O mínimo de respondentes vem da configuração da organização, com padrão de 3 (RN-005, P-03) |
| Transparência ao avaliado | Os objetivos, os indicadores e as datas dos check-ins são comunicados na abertura (RF-026). Se a organização usar pesos, eles aparecem com os critérios do cálculo (RN-008) |
| Critérios não discriminatórios | Objetivos, indicadores e perguntas tratam de comportamentos e resultados observáveis e não usam critérios como sexo, idade, raça ou estado civil (RN-001, RN-014) |
| Proteção contra erro | Resumo e confirmação antes de abrir o ciclo, porque a abertura notifica pessoas e fixa o questionário e os modos (RNF-015). Erros indicados com sugestão de correção (RNF-021) |
| Nada se perde | O planejamento incompleto fica salvo como ciclo planejado (RNF-012) |
| Trilha de auditoria | Abertura do ciclo, mudança de modo de identificação pelo RH e alterações depois da abertura ficam registradas (RNF-005) |
| Acessibilidade e responsividade | ABNT NBR 17225:2025 e WCAG 2.2 A e AA (RNF-017 a RNF-023). Uso em computador e celular (RNF-027) |

## 10. Lista de variações de tecnologia e dados

1. **Receptor do ciclo:** um ou mais colaboradores, ou uma equipe inteira (RF-022).
2. **Modalidades:** gestor → colaborador, ascendente, pares, equipe, autoavaliação e 360°, combináveis no mesmo ciclo (RF-024).
3. **Tipos de valor dos indicadores:** escala ordinal, valor numérico, atingido/não atingido ou texto livre (RF-009; E01 §27).
4. **Fontes de evidência dos indicadores:** por exemplo avaliação do cliente, avaliação do setor parceiro e pontualidade das entregas (E01 §5, §14).
5. **Notificações:** dentro do sistema e por e-mail (RF-026, DS-10).

## 11. Frequência de ocorrência

Uma vez por equipe a cada ciclo formal. A PO citou ciclos de 3 ou 4 meses (E01 §5), e os questionários indicam ciclos hoje anuais (Q01 §3). Com várias equipes, o RH vê alguns ciclos planejados por mês, concentrados no início de cada período.

## 12. Decisões de especificação

| # | Questão | Decisão | Justificativa |
|---|---|---|---|
| UC13-D01 | O que é copiado quando o Gestor parte de um ciclo anterior? | Objetivos, indicadores, competências, modalidades, questionários e modos de identificação. Avaliados, participantes e datas não são copiados | A PO quer reaproveitar parâmetros entre períodos (E01 §15), o que reduz a dor D2 do AS-IS 1. Avaliados e datas mudam a cada ciclo, e copiá-los criaria convites indevidos |
| UC13-D02 | O Gestor pode mudar o modo de identificação de uma modalidade? | Não. O Gestor usa o padrão de RN-004, e só o RH, ou o administrador, altera entre confidencial e anônimo | RF-030 dá essa configuração ao RH ou ao administrador. O gestor costuma ser o avaliado na avaliação ascendente, e escolher o modo dessa avaliação seria conflito de interesse (RN-004, decisão C-14 da lista geral) |
| UC13-D03 | O que pode mudar depois que o ciclo é aberto? | Pode: acrescentar participantes e avaliados, mudar as datas dos check-ins e prorrogar o prazo. Não pode: trocar o questionário nem o modo de identificação | Respostas já enviadas foram dadas para aquele questionário e sob aquele aviso de identificação (RF-019). Mudar depois tornaria as respostas incomparáveis ou quebraria o que foi prometido ao avaliador |
| UC13-D04 | O ciclo pode ser salvo sem ser aberto? | Sim, com o status **planejado** (`StatusCiclo.PLANEJADO` do modelo ER), sem notificar ninguém | O modelo ER já prevê o status. Permite revisar o planejamento antes de comunicar, e evita que o Gestor perca o que preencheu (RNF-012) |
| UC13-D05 | Todo objetivo precisa de indicador? | Sim, pelo menos um | A PO pede indicadores para traduzir objetivos amplos, como "melhorar a comunicação" (E01 §5, §29). Sem indicador o objetivo não pode ser medido nos check-ins (RF-023) |

## 13. Rastreabilidade

| Tipo | Itens |
|---|---|
| Requisitos funcionais | RF-010, RF-022, RF-023, RF-024, RF-025, RF-026, RF-030 (do diagrama); RF-005, RF-006, RF-007, RF-008, RF-009, RF-027, RF-029 (relacionados) |
| Requisitos não funcionais | RNF-005, RNF-012, RNF-015, RNF-017 a RNF-023, RNF-026, RNF-027 |
| Regras de negócio | RN-001, RN-004, RN-005, RN-007, RN-008, RN-014 |
| Entidades do modelo ER | `CicloAvaliacao`, `AvaliadoCiclo`, `CicloCompetencia`, `ObjetivoCiclo`, `Indicador`, `ModalidadeCiclo`, `Questionario`, `ConviteAvaliacao`, `CheckIn`, `ConfiguracaoOrganizacao`, `Notificacao`, `RegistroAuditoria` |
| Casos de uso relacionados | UC-01, UC-03, UC-04, UC-05 (cadastros prévios); UC-14 (resposta dos avaliadores); UC-15 (acompanhamento e encerramento); UC-18 (check-ins); UC-31 (notificações e lembretes) |
| Decisões aplicadas | P-01, P-03 (lista geral); DS-10 (especificação suplementar); M-04, M-05 (modelo ER) |
| Fontes | [Entrevista 01](../../../elicitacao/entrevistas/Entrevista01_Adriana.md), §5, §14, §15, §17, §19, §21 e §29; [Síntese dos questionários](../../../elicitacao/questionarios/Sintese.md); [Processo AS-IS e dores](../../../elicitacao/bpmn/Processo_AS-IS_e_Dores.md) |
