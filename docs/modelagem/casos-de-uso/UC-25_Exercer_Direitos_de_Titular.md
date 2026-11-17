# UC-25 Exercer direitos de titular

**Projeto:** Sistema Web de Feedback e Gestão de Competências
**Formato:** completo (Larman, cap. 6) · **Issue:** #48 · **Versão:** 1.0 · **Data:** 17/11/2026
**Responsável:** Verônica Ribeiro Oliveira Palmeira
**Prioridade:** Must · **Área:** Privacidade (LGPD) · [Diagrama](Diagrama_Casos_de_Uso.md#46-privacidade-lgpd) · [Modelo e convenções](Casos_de_Uso_Completos.md)

---

## 1. Escopo

Sistema Web de Feedback e Gestão de Competências.

## 2. Nível

Objetivo do usuário.

## 3. Ator principal

**Colaborador**, como titular dos seus dados pessoais. Gestores e usuários com perfil RH também usam este caso de uso para os próprios dados, porque o Gestor herda tudo o que o Colaborador faz (diagrama, seção 2).

## 4. Interessados e interesses

| Interessado | Interesse |
|---|---|
| **Colaborador (titular)** | Saber quais dados pessoais seus o sistema guarda, para que e com quem os compartilha. Ter acesso, cópia e correção de forma simples, gratuita e no prazo da lei. Pedir a eliminação do que for desnecessário (LGPD, arts. 18 e 19) |
| **Emissores de feedbacks e avaliações confidenciais ou anônimos** | Que o acesso do avaliado aos próprios dados não revele quem o avaliou. Os direitos de um titular não anulam os de outro (RF-056; pesquisa documental, seção 8, conflito 3) |
| **Organização contratante (controladora)** | Atender aos pedidos dos titulares no prazo e comprovar que atendeu (LGPD, art. 6º, X). Não perder o histórico oficial de feedbacks (RN-003) nem dados que a lei manda conservar (LGPD, art. 16) |
| **Encarregado de dados (DPO)** | Receber cada pedido completo, com tipo, prazo e histórico, para respondê-lo no UC-27 (RF-061; LGPD, art. 41, §2º, I) |
| **RH** | Nas organizações sem encarregado, tratar os pedidos dos titulares (RF-061). É também o único perfil que consegue consultar o vínculo de um emissor confidencial (RN-004) |

## 5. Pré-condições

1. O Colaborador está autenticado (RF-003).
2. O aviso de privacidade está publicado e as categorias de dados têm finalidade, base legal e prazo de retenção cadastrados (UC-28; RF-053, RF-054, RF-062).

## 6. Garantia de sucesso (pós-condições)

1. O Colaborador recebeu na hora a resposta que o sistema pode dar sozinho (consulta, cópia exportada ou lista de compartilhamentos) **ou** tem um pedido registrado com número de protocolo, tipo, data de abertura, prazo e situação "aberta", na fila do encarregado e do RH (RF-061).
2. Nenhum dado foi alterado, eliminado ou anonimizado por este caso de uso. Isso só acontece depois da análise do pedido, no UC-27.
3. Nenhuma informação entregue ao Colaborador revela a identidade de emissores confidenciais ou anônimos (RF-056, RN-004, RN-005).
4. A operação foi registrada na trilha de auditoria (RNF-005).

## 7. Cenário de sucesso principal

O cenário mostra o caso mais completo: o Colaborador consulta seus dados e pede a declaração completa, que depende de análise humana.

1. O Colaborador pede para consultar seus dados pessoais.
2. O Sistema confirma que trata dados do Colaborador e apresenta, na hora, um resumo organizado por categoria (cadastro, feedbacks recebidos, avaliações, metas, planos de ação e consentimentos), com a finalidade, a base legal e o prazo de retenção de cada categoria (RF-056, RF-054). Mostra também as entidades com quem os dados foram compartilhados (RF-060) e os direitos que o Colaborador pode exercer (RF-053).
3. O Colaborador pede a declaração completa dos seus dados, com origem, critérios e finalidade do tratamento (RF-056).
4. O Sistema registra o pedido com número de protocolo, tipo, data de abertura, prazo de 15 dias e situação "aberta" (LGPD, art. 19, II), e o coloca na fila de solicitações de titulares (RF-061).
5. O Sistema notifica o encarregado e o RH de que há um novo pedido na fila (DS-10).
6. O Sistema informa ao Colaborador o número de protocolo, a data de abertura e o prazo de resposta.
7. O Sistema registra a operação na trilha de auditoria (RNF-005).

O pedido é tratado no UC-27. Quando a resposta é registrada, o Sistema notifica o Colaborador, que a consulta pela extensão 1a.

## 8. Extensões

**\*a. A qualquer momento, o Colaborador quer ler o aviso de privacidade ou o contato do encarregado.**

1. O Sistema apresenta o aviso de privacidade, com finalidades, bases legais, compartilhamentos, prazos de retenção, direitos do titular e identidade e contato do encarregado (RF-053).
2. O cenário continua de onde parou.

**1a. O Colaborador quer acompanhar um pedido feito antes.**

1. O Sistema lista os pedidos do Colaborador, com protocolo, tipo, data de abertura, prazo, situação e, quando houver, a resposta (RF-061).
2. O Colaborador consulta o pedido que escolheu.
3. O caso de uso termina.

**2a. Entre os dados do Colaborador há feedbacks ou avaliações vindos de modalidades confidenciais ou anônimas.**

1. O Sistema apresenta esses feedbacks sem a identidade do emissor e mostra os resultados dessas modalidades só de forma consolidada, quando há o número mínimo de respondentes (RF-056, RN-004, RN-005; UC25-D03).
2. O cenário continua no passo 3.

**3a. A consulta do passo 2 basta ao Colaborador.**

1. O Sistema registra a consulta na trilha de auditoria (RNF-005).
2. O caso de uso termina.

**3b. O Colaborador quer uma cópia dos seus dados (portabilidade).**

1. O Colaborador escolhe o formato, JSON ou CSV (RF-058).
2. O Sistema gera o arquivo com o cadastro, os feedbacks recebidos, as metas e os planos de ação do Colaborador, com a mesma proteção dos emissores da extensão 2a (RF-058).
3. O Sistema entrega o arquivo ao Colaborador e registra a exportação na trilha de auditoria (RNF-005).
4. O caso de uso termina.

**3c. O Colaborador quer corrigir um dado cadastral incompleto, inexato ou desatualizado.**

1. O Colaborador indica o dado e informa o valor correto (RF-057).
2. O Sistema registra um pedido de correção, com prazo e situação "aberta", e o coloca na fila (RF-061).
3. O cenário continua no passo 5.

**3d. O Colaborador quer corrigir o conteúdo de um feedback que recebeu.**

1. O Sistema informa que o texto de um feedback pertence ao emissor e não pode ser alterado pelo receptor (RN-003), e que o Colaborador pode registrar a sua manifestação em uma réplica (RF-020; UC25-D02).
2. O Colaborador escolhe registrar a réplica, e o fluxo segue no UC-10, **ou** desiste, e o caso de uso termina.

**3e. O Colaborador quer a anonimização, o bloqueio ou a eliminação de dados.**

1. O Colaborador indica os dados e o motivo do pedido (RF-059).
2. O Sistema informa, antes de registrar o pedido, que alguns dados podem ser conservados pela organização: o histórico oficial de feedbacks durante o prazo de retenção (RN-003, RN-011), os dados que a lei manda guardar (LGPD, art. 16) e os dados sob bloqueio por processo judicial (RF-062).
3. O Colaborador confirma o pedido.
4. O Sistema registra o pedido, com prazo e situação "aberta", e o coloca na fila (RF-061). Nenhum dado é alterado nesse momento (UC25-D04).
5. O cenário continua no passo 5.

**3f. O Colaborador quer revogar um consentimento dado antes.**

1. O fluxo segue no UC-26 Gerenciar consentimentos (RF-055).

**3g. O Colaborador quer um esclarecimento sobre os compartilhamentos que não está na lista do passo 2.**

1. O Colaborador descreve a dúvida.
2. O Sistema registra um pedido de informação sobre compartilhamento, com prazo e situação "aberta", e o coloca na fila (RF-060, RF-061).
3. O cenário continua no passo 5.

**4a. O Sistema não consegue registrar o pedido.**

1. O Sistema informa que o pedido não foi registrado e mantém o que o Colaborador preencheu, para que ele tente de novo (RNF-021).
2. O cenário volta ao passo do pedido que estava sendo feito.

## 9. Requisitos especiais

| Requisito | Como se aplica a este caso de uso |
|---|---|
| Prazos da LGPD | Consulta simplificada na hora. Declaração completa em até 15 dias contados do pedido (LGPD, art. 19, I e II). O prazo de cada pedido aparece para o Colaborador e na fila |
| Gratuidade | Nenhum pedido tem custo para o titular (LGPD, art. 18, §5º) |
| Linguagem clara | As informações sobre o tratamento são apresentadas de forma clara e em português do Brasil (LGPD, arts. 6º, VI, e 9º; RNF-016) |
| Proteção dos emissores | Em nenhum ponto o Colaborador vê a identidade de emissores confidenciais ou anônimos, inclusive quando ele tem perfil RH e é o avaliado (RN-004, RN-005) |
| Trilha de auditoria | Toda consulta, exportação e pedido gera registro inalterável de quem, quando, o quê e de onde (RNF-005) |
| Segurança | O arquivo exportado só trafega por conexão criptografada (RNF-004). A sessão segue os limites de RNF-006 (DS-05) |
| Formato da exportação | Estruturado e legível por máquina (RF-058) |
| Acessibilidade e responsividade | ABNT NBR 17225:2025 e WCAG 2.2 A e AA (RNF-017 a RNF-023). Uso em computador e celular (RNF-027) |

## 10. Lista de variações de tecnologia e dados

1. Exportação dos dados em **JSON** ou **CSV** (RF-058).
2. Notificação ao encarregado, ao RH e ao Colaborador **dentro do sistema e por e-mail** (DS-10).
3. Uso por **navegador** em computador ou celular: Chrome, Edge, Firefox e Safari, na versão atual e na anterior (RNF-030, DS-07).

## 11. Frequência de ocorrência

Eventual. Depende da iniciativa de cada titular, e as fontes do levantamento não trazem estimativa de volume. A consulta simplificada (passo 2) deve ser a forma mais comum, porque é a única que não depende de pedido.

## 12. Decisões de especificação

| # | Questão | Decisão | Justificativa |
|---|---|---|---|
| UC25-D01 | Quais direitos o sistema atende sozinho e quais viram pedido na fila? | Atende na hora a consulta simplificada, a exportação e a lista de compartilhamentos. Registra como pedido na fila a declaração completa, a correção, a anonimização, o bloqueio, a eliminação e os esclarecimentos sobre compartilhamento | A lei pede a consulta simplificada "imediatamente" (art. 19, I), e RF-058 e RF-060 descrevem funções que o próprio colaborador usa. Os demais pedidos dependem de análise de quem responde pelo tratamento (RF-061; LGPD, art. 18, §§3º e 4º). O tipo `TipoSolicitacaoTitular` do modelo ER cobre todos os tipos de pedido |
| UC25-D02 | O direito de correção (art. 18, III) vale para o texto de um feedback recebido? | Não. Vale para os dados cadastrais (RF-057). Para discordar de um feedback, o receptor registra uma réplica | O texto do feedback é a manifestação do emissor, e só ele pode editá-lo, com versões (RN-003). A pesquisa documental liga o direito de correção à réplica (seção 3.4; RD-09, hoje RF-020) |
| UC25-D03 | O que o avaliado vê dos feedbacks e avaliações confidenciais ou anônimos? | O conteúdo sem a identidade do emissor e, nos resultados de ciclo, só valores consolidados com o mínimo de respondentes | RF-056 e a decisão da pesquisa documental para o conflito entre o direito de acesso e a proteção do emissor confidencial (seção 8, conflito 3). Sem o mínimo de respondentes, o emissor poderia ser descoberto por exclusão (RN-005) |
| UC25-D04 | O pedido de eliminação é executado na hora? | Não. O pedido é registrado e analisado no UC-27. O Colaborador é avisado antes das hipóteses de conservação | O feedback é registro oficial e não pode ser excluído durante a retenção (RN-003, RN-011). A lei permite conservar dados nas hipóteses do art. 16, e o bloqueio por processo judicial suspende a eliminação (RF-062) |
| UC25-D05 | As respostas que o próprio Colaborador emitiu em avaliações confidenciais ou anônimas aparecem nos seus dados? | As anônimas não, porque nada as liga a ele. As confidenciais entram só na declaração completa, preparada no UC-27 | Dado anonimizado não é dado pessoal (LGPD, art. 12) e o modelo ER não guarda vínculo no modo anônimo (seção 10). No modo confidencial, o vínculo só pode ser consultado pelo RH, com registro na auditoria (RN-004, RNF-003) |
| UC25-D06 | Como exerce os direitos quem não tem mais acesso ao sistema, como um colaborador desligado? | Pelo contato do encarregado divulgado no aviso de privacidade. O encarregado registra o pedido na fila e o trata no UC-27 | Os dados ficam guardados após o desligamento (RN-011), e o titular continua com os direitos do art. 18. Receber as comunicações dos titulares é atribuição do encarregado (LGPD, art. 41, §2º, I). Este caso de uso parte de um Colaborador autenticado (pré-condição 1) |

## 13. Rastreabilidade

| Tipo | Itens |
|---|---|
| Requisitos funcionais | RF-053, RF-056, RF-057, RF-058, RF-059, RF-060 (do diagrama); RF-020, RF-055, RF-061 (casos relacionados) |
| Requisitos não funcionais | RNF-004, RNF-005, RNF-006, RNF-016, RNF-017 a RNF-023, RNF-027, RNF-030, RNF-031 |
| Regras de negócio | RN-003, RN-004, RN-005, RN-011, RN-012 |
| Entidades do modelo ER | `SolicitacaoTitular`, `CategoriaDado`, `CompartilhamentoDados`, `BloqueioLegal`, `Consentimento`, `RegistroAuditoria`, `Notificacao`, `VinculoConfidencial` |
| Casos de uso relacionados | UC-10 (réplica, extensão 3d), UC-26 (consentimento, extensão 3f), UC-27 (tratamento dos pedidos), UC-28 (configuração da privacidade, pré-condição) |
| Decisões aplicadas | DS-05, DS-07, DS-10 (especificação suplementar) |
| Fontes | LGPD, arts. 6º, 9º, 12, 16, 18, 19 e 41 (FD-01); [Pesquisa Documental](../../elicitacao/pesquisa-documental/Pesquisa_Documental.md), seções 3.4 e 3.5 e conflito 3 da seção 8 |
