# UC-19 Criar plano de ação

**Projeto:** Sistema Web de Feedback e Gestão de Competências
**Formato:** completo (Larman, cap. 6) · **Issue:** #48 · **Versão:** 1.1 · **Data:** 17/11/2026
**Responsável:** Ana Luísa Pereira dos Santos
**Prioridade:** Must · **Área:** Plano de ação e metas · [Diagrama](Diagrama_Casos_de_Uso.md#44-plano-de-ação-e-metas) · [Modelo e convenções](Casos_de_Uso_Completos.md)

---

## 1. Escopo

Sistema Web de Feedback e Gestão de Competências.

## 2. Nível

Objetivo do usuário. Estende o UC-08 Registrar feedback, no ponto de extensão "depois de registrar um feedback construtivo" (diagrama, seção 5).

## 3. Ator principal

**Gestor (emissor)**: quem deu o feedback construtivo e conduz a definição do plano. Na maior parte dos casos é o gestor direto do receptor (E01 §4; E02 §4). O **receptor** do feedback participa como ator de apoio, porque o plano é definido em conjunto (RN-006).

## 4. Interessados e interesses

| Interessado | Interesse |
|---|---|
| **Emissor (gestor)** | Transformar o feedback construtivo em um combinado com ações, metas e pontos de verificação, e saber depois se a pessoa melhorou. Hoje "eu não tenho controle se houve uma melhora" (E01 §6; dor D4 do AS-IS 1), e o acompanhamento depende de anotações e da memória (E02 §4; dor D4 do AS-IS 2) |
| **Receptor** | Participar da definição do plano, que é "produto da colaboração dos dois" (E01 §4; RN-006). Propor as próprias soluções, a partir da autorreflexão (E01 §4). Ter ações e prazos claros e possíveis de cumprir. Ver o plano como apoio ao desenvolvimento, e não como punição (RN-007) |
| **Gestor direto do receptor** (quando não é o emissor) | Acompanhar os planos de ação da sua equipe (RF-044) |
| **RH** | Acompanhar os planos de toda a organização (RF-044) e saber quais feedbacks e planos resultaram em melhora (RF-045; E01 §4) |
| **Organização contratante** | Feedback que gera mudança de comportamento e resultado, com histórico confiável (RF-048). Dados tratados só para a finalidade de desenvolvimento (RN-013, RN-015) |

## 5. Pré-condições

1. O Gestor está autenticado (RF-003).
2. Há um feedback **construtivo** registrado pelo Gestor no UC-08, com fatos vinculados e o campo de reflexão da estrutura do construtivo (RF-013, RF-016, RN-002).
3. Esse feedback ainda não tem plano de ação (modelo ER: um feedback origina no máximo um plano).

## 6. Garantia de sucesso (pós-condições)

1. O plano de ação foi gravado, ligado ao feedback construtivo de origem, com o emissor e o receptor (RF-042, RN-006).
2. O plano tem pelo menos uma ação, cada uma com descrição, responsável, meta e prazo, pelo menos um ponto de monitoramento e a data final (RF-042).
3. O receptor confirmou o plano, e o plano está **aberto** para acompanhamento no UC-20 (RN-006; UC19-D01).
4. Os lembretes dos pontos de monitoramento e da data final foram programados para o emissor e o receptor, salvo para quem desativou lembretes (RF-040, UC-31).
5. O plano aparece no histórico do receptor e na visão de planos do gestor direto e do RH (RF-044, RF-048), e só para as pessoas que podem ver o feedback de origem (RNF-001).

## 7. Cenário de sucesso principal

1. Depois de registrar um feedback construtivo no UC-08, o Gestor pede para criar o plano de ação desse feedback.
2. O Sistema apresenta o feedback de origem, com os fatos, o problema, a repercussão e a reflexão registrados, e as competências relacionadas (RF-016, RF-021).
3. O Gestor e o receptor, normalmente na sessão de feedback, combinam as ações a partir da autorreflexão do receptor (E01 §4).
4. O Gestor registra cada ação, com descrição, responsável, meta e prazo (RF-042).
5. O Gestor define os pontos de monitoramento, com a data de cada um, e a data final do plano (RF-042; E01 §4).
6. O Sistema confere o plano e apresenta o resumo (RNF-015).
7. O Gestor envia o plano ao receptor para confirmação.
8. O Sistema avisa o receptor de que há um plano de ação para confirmar (UC19-D01).
9. O receptor consulta o plano e confirma que ele corresponde ao que foi combinado (RN-006).
10. O Sistema grava o plano como **aberto**, programa os lembretes dos pontos de monitoramento e da data final e avisa o Gestor da confirmação (RF-040; DS-10).
11. O Sistema confirma ao Gestor e ao receptor que o plano está em acompanhamento e o mostra no histórico do receptor (RF-048). O acompanhamento segue no UC-20.

## 8. Extensões

**\*a. A qualquer momento, o Gestor interrompe o registro ou a sessão expira.**

1. O Sistema mantém o plano como rascunho, visível só para o Gestor (RNF-012, RNF-002).
2. Quando o Gestor volta ao feedback de origem, o cenário continua no passo em que parou.

**1a. O feedback de origem é positivo.**

1. O Sistema informa que o plano de ação nasce de um feedback construtivo e sugere cadastrar uma meta de desenvolvimento (RF-042; UC-21).
2. O caso de uso termina.

**1b. O feedback de origem já tem um plano de ação.**

1. O Sistema apresenta o plano existente.
2. O caso de uso termina, e o Gestor pode acompanhá-lo no UC-20.

**1c. O Gestor prefere criar o plano depois, na sessão de feedback.**

1. O Gestor adia a criação. O Sistema mantém, no feedback de origem, a indicação de que o plano ainda não foi criado.
2. O caso de uso termina. O Gestor pode retomá-lo a partir do feedback, ou agendar a sessão no UC-11.

**1d. O emissor do feedback construtivo não é o gestor do receptor, como um par ou um colega de outra área, e o feedback é identificado.**

1. O Sistema permite ao emissor criar o plano com o receptor, da mesma forma que o Gestor (RF-042, RN-006).
2. O Sistema informa que o gestor direto do receptor também acompanhará o plano (RF-044).
3. O cenário continua no passo 2.

**1e. O feedback de origem é confidencial, como o de um par ou o da avaliação ascendente.**

1. O Sistema informa ao emissor que o plano será definido pelo receptor e pelo gestor direto do receptor, sem o emissor, para não revelar quem emitiu (RN-004, RN-006; UC19-D04).
2. O caso de uso termina para o emissor. O gestor direto do receptor, que já pode ver o feedback (RNF-001), cria o plano a partir do feedback de origem, seguindo este cenário a partir do passo 2 no lugar do emissor.

**3a. O emissor e o receptor não chegam a um acordo sobre as ações.**

1. O Gestor registra no plano as ações em que houve acordo e deixa os demais pontos para um novo feedback ou para a próxima sessão (UC-11).
2. O cenário continua no passo 4, com as ações acordadas.

**4a. O Gestor indica como responsável de uma ação alguém que não é o emissor nem o receptor.**

1. O Sistema informa que os responsáveis pelas ações são o receptor ou o emissor, porque o plano só é visto por quem pode ver o feedback de origem (RNF-001; UC19-D02).
2. O cenário volta ao passo 4.

**4b. Uma ação depende de uma competência específica que o receptor ainda não tem atribuída.**

1. O Gestor pode atribuir a competência ao receptor (UC-04, RF-006).
2. O cenário continua no passo 4.

**5a. Um ponto de monitoramento fica depois da data final, ou a data final já passou.**

1. O Sistema indica as datas com problema e sugere a correção (RNF-021).
2. O cenário volta ao passo 5.

**6a. Falta um campo obrigatório: ação sem responsável, meta ou prazo, plano sem ponto de monitoramento ou sem data final.**

1. O Sistema identifica cada campo com problema e sugere a correção (RNF-021).
2. O cenário volta ao passo 4.

**6b. Um texto contém termo da lista de termos ofensivos ou discriminatórios mantida pelo administrador (Could).**

1. O Sistema destaca o trecho e sugere a revisão, sem bloquear o envio (RNF-024, DS-13).
2. O Gestor revisa o texto, e o cenário volta ao passo 4, **ou** mantém o texto, e o cenário continua no passo 7.

**9a. O receptor pede ajustes ao plano.**

1. O receptor registra o que quer ajustar.
2. O Sistema avisa o Gestor do pedido.
3. O Gestor ajusta o plano, e o cenário volta ao passo 6.

**9b. O receptor não confirma o plano até o primeiro ponto de monitoramento.**

1. O Sistema lembra o receptor e o Gestor de que o plano ainda não foi confirmado (RF-040, UC-31).
2. O plano continua aguardando confirmação, e o cenário continua no passo 9 quando o receptor o consultar.

**10a. O Sistema não consegue gravar a confirmação.**

1. O Sistema informa que a confirmação não foi registrada e mantém o plano aguardando confirmação.
2. O cenário volta ao passo 9.

## 9. Requisitos especiais

| Requisito | Como se aplica a este caso de uso |
|---|---|
| Visibilidade | O plano tem o mesmo público do feedback de origem: receptor, emissor, gestor direto do receptor e RH (RNF-001). Enquanto é rascunho, só o emissor o vê (RNF-002) |
| Definição em conjunto | O plano só fica aberto depois da confirmação do receptor (RN-006; UC19-D01) |
| Desenvolvimento, não punição | O plano não gera consequência automática sobre o receptor. Se o histórico for usado em decisões sobre pessoas, os critérios precisam ser documentados e iguais para todos no mesmo cargo (RN-007, RN-008) |
| Conteúdo dos textos | Ações e metas descrevem comportamentos e resultados observáveis, sem dados sensíveis nem de saúde (RN-001, RN-013, RN-015; RF-018) |
| Lembretes | Pontos de monitoramento e data final geram lembretes, que cada usuário pode desativar (RF-040) |
| Nada se perde | O plano incompleto fica como rascunho (RNF-012) |
| Proteção contra erro | Resumo antes do envio ao receptor (RNF-015) e erros indicados com sugestão de correção (RNF-021) |
| Acessibilidade e responsividade | ABNT NBR 17225:2025 e WCAG 2.2 A e AA (RNF-017 a RNF-023). Uso em computador e celular (RNF-027) |

## 10. Lista de variações de tecnologia e dados

1. **Momento da criação:** logo depois de registrar o feedback, ou mais tarde, na sessão de feedback (E01 §4; UC-08).
2. **Responsável de cada ação:** o receptor, na maior parte das ações, ou o emissor, por exemplo quando o gestor se compromete a dar um treinamento ou um retorno (UC19-D02).
3. **Avisos e lembretes:** dentro do sistema e por e-mail (RF-040, DS-10).
4. **Uso:** por navegador em computador ou celular, inclusive durante a sessão de feedback (RNF-027, RNF-030).

## 11. Frequência de ocorrência

Uma vez por feedback construtivo que precisa de correção. A PO diz que, no construtivo, "geralmente" se faz um plano de ação (E01 §4). A E02 diz que a conversa termina "com um combinado de melhoria" (E02 §4). O feedback construtivo é mais frequente que o positivo (E01 §20; E02 §2).

## 12. Decisões de especificação

| # | Questão | Decisão | Justificativa |
|---|---|---|---|
| UC19-D01 | Como o sistema registra que o plano foi definido em conjunto? | O emissor registra o plano e o receptor confirma. O plano só fica aberto depois da confirmação. **Impacto no modelo ER (#52), aplicado na versão 1.1 do modelo:** acrescentar o valor `AGUARDANDO_CONFIRMACAO` à enumeração `StatusPlano` e o valor `PLANO_PARA_CONFIRMAR` à `TipoNotificacao` | RN-006 exige a definição conjunta, e a PO descreve o plano como "produto da colaboração dos dois" (E01 §4). Sem a confirmação, nada distingue um plano combinado de um plano imposto pelo emissor |
| UC19-D02 | Quem pode ser responsável por uma ação? | Só o receptor ou o emissor do feedback. No plano de feedback confidencial, o gestor direto ocupa o lugar do emissor (UC19-D04) | O plano mostra o problema do feedback construtivo. Pela RNF-001, só o receptor, o emissor, o gestor direto e o RH podem ver esse conteúdo. Um terceiro como responsável teria acesso ao plano e, com ele, ao problema |
| UC19-D03 | O plano pode ser criado depois do envio do feedback? | Sim, a partir do feedback de origem, enquanto ele não tiver plano | A PO descreve o plano como resultado da sessão de feedback, depois da autorreflexão do receptor (E01 §4). Exigir o plano no mesmo momento do registro obrigaria a decidir antes da conversa |
| UC19-D04 | Quem define o plano quando o feedback construtivo é confidencial? | O receptor e o seu gestor direto, sem o emissor. O plano guarda o gestor direto no lugar do emissor (`PlanoAcao.gestor_id` no modelo ER 1.1) | Decisão ERS-D05 da especificação IEEE 830, incorporada à RN-006 na lista geral 1.1. A RN-004 proíbe revelar o emissor confidencial ao receptor, e um plano conjunto com o emissor o revelaria. O gestor direto já pode ver o feedback (RNF-001), então nenhum dado novo é exposto |

## 13. Rastreabilidade

| Tipo | Itens |
|---|---|
| Requisitos funcionais | RF-042 (do diagrama); RF-006, RF-013, RF-016, RF-018, RF-021, RF-040, RF-043, RF-044, RF-045, RF-048 (relacionados) |
| Requisitos não funcionais | RNF-001, RNF-002, RNF-012, RNF-015, RNF-017 a RNF-023, RNF-024, RNF-027, RNF-030 |
| Regras de negócio | RN-001, RN-004, RN-006, RN-007, RN-008, RN-013, RN-015 |
| Entidades do modelo ER | `PlanoAcao`, `AcaoPlano`, `PontoMonitoramento`, `Feedback`, `FeedbackFato`, `FeedbackCompetencia`, `Notificacao` |
| Casos de uso relacionados | UC-08 (feedback construtivo, caso estendido); UC-04 (competências específicas); UC-11 (sessão de feedback); UC-20 (acompanhamento do plano); UC-21 (metas de desenvolvimento); UC-31 (lembretes) |
| Decisões aplicadas | DS-10, DS-13 (especificação suplementar); ERS-D05 (especificação IEEE 830) |
| Fontes | [Entrevista 01](../../elicitacao/entrevistas/Entrevista01_Adriana.md), §4, §6 e §20; [Entrevista 02](../../elicitacao/entrevistas/Entrevista02_Eliene.md), §2 e §4; [Processo AS-IS e dores](../../elicitacao/bpmn/Processo_AS-IS_e_Dores.md) |
