# Planejamento da 2ª etapa e tabela de autoria e revisão

**Projeto:** Sistema Web de Feedback e Gestão de Competências · **Etapa:** 2ª Entrega – Arquitetura e Desenho Detalhado · **Prazo:** 08/12/2026
**Versão:** 1.2 · **Issue:** #78 · **Autora:** Isadora Yasmim da Silva · **Revisor(a):** Júlia de Souza Nascimento

| Item | Descrição |
|---|---|
| Tipo e natureza | Tabela de controle (planejamento), não é modelo do sistema |
| Propósito | Distribuir os artefatos da 2ª etapa entre os integrantes e registrar quem é autor e quem é revisor de cada um, conforme as regras 3 e 4 da seção 7 do enunciado |
| Público-alvo | Integrantes do grupo e a docente/PO |
| Uso no documento final | A tabela da seção 3 entra no PDF depois dos apêndices, como tabela **artefato · autor · revisor** (issue #109) |

---

## 1. Regras atendidas

| Regra (seção 7 do enunciado) | Como este documento atende |
|---|---|
| 3. A mesma pessoa não pode ser autora e revisora do mesmo item | Cada linha da seção 3 tem autor e revisor diferentes; a conferência está na seção 4 |
| 3. Todo integrante é autor de algum item e revisor de outro | A seção 4 mostra a quantidade de itens de cada integrante nos dois papéis |
| 4. O documento final traz a tabela artefato, autor e revisor | A seção 3 é essa tabela, mantida aqui até a consolidação do PDF |
| 7. A docente faz parte do time do GitHub e do Discord | Convite do GitHub enviado e servidor do Discord criado; situação registrada na seção 5 |

A revisão de cada item é feita no pull request da issue correspondente: o revisor indicado aprova o PR, e só então o merge é feito. O PR aprovado é a evidência de revisão.

---

## 2. Critérios da distribuição

1. **Carga equilibrada:** cada integrante soma entre 13 e 14 itens, como autor ou como revisor.
2. **Revisor que conhece o artefato vizinho:** sempre que possível, o revisor é autor de um artefato que precisa ser coerente com o revisado, para que a revisão confira também o checklist de consistência (Apêndice 2 do enunciado). Exemplos: o autor do DImp revisa o DPac; o autor dos DSeq de operação revisa os contratos; quem fez o dicionário de dados na 1ª etapa revisa os protótipos.
3. **Revisão cruzada entre os níveis do C4:** quem modela um nível revisa o nível vizinho, o que ajuda a manter os componentes coerentes entre DImp, DPac, DCmp e DCla.

---

## 3. Tabela artefato × autor × revisor

Os identificadores seguem a convenção que será fixada no guia de padrões (#79). A coluna **Seção do PDF** indica onde o artefato entra no documento único.

| Issue | Artefato | Seção do PDF | Autor(a) | Revisor(a) | Critério do revisor |
|---|---|---|---|---|---|
| **Planejamento e padrões** ||||||
| #78 | Planejamento da 2ª etapa e tabela de autoria e revisão (este documento) | Após os apêndices | Isadora | Júlia | Consolida o PDF que recebe a tabela |
| #79 | Guia de padrões da arquitetura (`Padroes.md`) | — (uso interno) | Davi | Isadora | Aplica os padrões no DPac, DCmp e DCla |
| #80 | Decisões arquiteturais e stack (`Decisoes_Arquiteturais.md`) | 3 | Isadora | Verônica | Autora dos RNF e mecanismos (seção 3) |
| **Seções textuais** ||||||
| #81 | Seção 1 – Introdução | 1 | Ana Luísa | Júlia | Visão geral do documento consolidado |
| #82 | Seção 2 – Stakeholders, preocupações e matriz | 2 | Davi | Ana Luísa | Conduziu a elicitação na 1ª etapa |
| #83 | Seção 3 – RNF (ISO/IEC 25010) e mecanismos arquiteturais | 3 | Verônica | Isadora | Autora das decisões arquiteturais |
| #84 | Seção 4.1 – Browser, servidor web, servidor de aplicação e HTTP | 4 | Verônica | Davi | Autor do DImp (nós e protocolos) |
| #85 | Seção 4.2 – Ciclo completo da requisição e formas de invocação | 4 | Verônica | Davi | Autor do DImp e dos DSeq entre componentes |
| #86 | Seção 4.3 – Sessão e manutenção de estado | 4 | Verônica | Isadora | Autora da stack (mecanismo de sessão) |
| **N1 – Contexto** ||||||
| #87 | DImp-01 – Diagrama de implantação com atores | 5 (N1) | Davi | Isadora | Autora da stack e do DPac |
| #88 | DPN-01 a DPN-04 – Processos de negócio TO-BE | 5 (N1) | Ana Luísa | Davi | Autor dos DCdu (atores e fluxos) |
| #89 | DCdu-01 a DCdu-08 – Diagramas de casos de uso | 5 (N1) | Davi | Júlia | Autora de 11 casos de uso completos |
| **N2 – Containers** ||||||
| #90 | DPac-01 – Diagrama de pacotes | 5 (N2) | Isadora | Davi | Autor do DImp (coerência DImp ↔ DPac) |
| #91 | Casos de uso completos – grupo 4.1 (UC-01 a UC-05) | 5 (N2) | Júlia | Verônica | Autora dos RNF e da especificação IEEE 830 |
| #92 | Casos de uso completos – grupo 4.2 (UC-06, UC-07, UC-09 a UC-12) | 5 (N2) | Júlia | Davi | Autor do UC-08, do mesmo grupo |
| #93 | Casos de uso completos – grupo 4.3 (UC-15 a UC-18) | 5 (N2) | Davi | Júlia | Autora do UC-13, do mesmo grupo |
| #94 | Casos de uso completos – grupos 4.4 e 4.5 (UC-20 a UC-24) | 5 (N2) | Ana Luísa | Verônica | Autora da especificação IEEE 830 |
| #95 | Casos de uso completos – grupos 4.6 e 4.7 (UC-26 a UC-31) | 5 (N2) | Verônica | Ana Luísa | Autora do dicionário de dados (inventário LGPD) |
| #96 | PIhc-01 a PIhc-31 – Protótipo de IHC por caso de uso | 5 (N2) | Júlia | Ana Luísa | Confere os dados das telas com o dicionário |
| **N3 – Componentes** ||||||
| #97 | DCmp do backend | 5 (N3) | Isadora | Júlia | Autora do DCmp do frontend (interfaces entre os dois) |
| #98 | DCmp do frontend | 5 (N3) | Júlia | Isadora | Autora do DCmp do backend |
| #99 | ECBD – DCD/MER e DDC por pacote | 5 (N3) | Ana Luísa | Isadora | Autora do modelo ER da 1ª etapa |
| #100 | DSeq entre componentes – parte 1 (feedback e ciclo de avaliação) | 5 (N3) | Davi | Ana Luísa | Autora da parte 2 (mesma notação e componentes) |
| #101 | DSeq entre componentes – parte 2 (autenticação, organização, planos, painéis e LGPD) | 5 (N3) | Ana Luísa | Davi | Autor da parte 1 |
| **N4 – Código** ||||||
| #102 | EOBD – tabelas, tipos e tamanhos | 5 (N4) | Ana Luísa | Verônica | Confere tamanhos e tipos com os RNF de segurança e LGPD |
| #103 | DCla – diagramas de classes por componente | 5 (N4) | Isadora | Ana Luísa | Autora do ECBD e do EOBD (classes ↔ tabelas) |
| #104 | DSeq de operações de classe (3) | 5 (N4) | Isadora | Verônica | Autora dos contratos das mesmas operações |
| #105 | CTR-01 a CTR-03 – Contratos de operação (Larman, cap. 11) | 5 (N4) | Verônica | Isadora | Autora dos DSeq e do DCla das mesmas operações |
| **Rastreabilidade, referências e consolidação** ||||||
| #106 | Matriz de rastreabilidade da arquitetura e verificação de consistência | 2 e apêndice | Davi | Verônica | Analista de qualidade; fará a revisão final |
| #107 | Referências e apêndice de prompts de IA | Referências e Apêndice II | Isadora | Ana Luísa | Autora do apêndice de reuniões (mesmo formato) |
| #108 | Apêndice de reuniões, comunicações e riscos | Apêndice | Ana Luísa | Júlia | Organiza a apresentação e o PDF |
| #109 | Documento único em PDF | Todas | Júlia | Verônica | Faz a revisão final da arquitetura |
| #110 | Revisão final da arquitetura e consolidação (`docs/arquitetura/Revisao_Final.md`) | — | Verônica | Júlia | Consolida o PDF com as correções da revisão |
| #111 | Apresentação final e avaliação 360º | — | Júlia | Ana Luísa | Autora da introdução (visão geral do sistema) |

---

## 4. Conferência das regras

### 4.1 Autor diferente do revisor (regra 3)

Nas 34 linhas da seção 3, autor e revisor são pessoas diferentes. A conferência foi feita por script sobre a tabela e deve ser repetida a cada mudança de responsável.

### 4.2 Itens por integrante

| Integrante | Usuário no GitHub | Autor(a) | Revisor(a) | Total |
|---|---|---|---|---|
| Ana Luísa Pereira dos Santos | `AnaLuisaPS07` | 7 | 7 | 14 |
| Davi Augusto Ferreira de Carvalho | `DaviAugusto778` | 7 | 6 | 13 |
| Isadora Yasmim da Silva | `isadora-yasmim` | 7 | 7 | 14 |
| Júlia de Souza Nascimento | `jusouzn` | 6 | 7 | 13 |
| Verônica Ribeiro Oliveira Palmeira | `Veronicapalmeira` | 7 | 7 | 14 |
| **Total** | | **34** | **34** | **68** |

Todos os integrantes são autores de pelo menos um item e revisores de pelo menos um outro.

---

## 5. Pendências do planejamento

| # | Pendência | Responsável | Situação em 19/11/2026 |
|---|---|---|---|
| 1 | Ler o enunciado da Parte III em grupo e levar as dúvidas à PO | Todos | A fazer na próxima reunião; registrar na ata (#108) |
| 2 | Confirmar esta distribuição de revisores com o grupo | Todos | **Concluída:** distribuição confirmada pelo grupo e campo **Revisor(a)** preenchido nas issues #78 a #111 |
| 3 | Docente como colaboradora do repositório no GitHub (regra 7) | Isadora | **Aguardando a docente:** convite enviado e ainda não aceito. Enquanto isso, o repositório fica público para que ela tenha acesso |
| 4 | Docente no servidor do Discord (regra 7) | Isadora | **Aguardando a docente:** servidor da equipe criado; o convite será enviado assim que a docente informar o usuário dela no Discord |

---

## 6. Histórico de versões

| Versão | Data | Autor(a) | Alteração |
|---|---|---|---|
| 1.0 | 19/11/2026 | Isadora Yasmim da Silva | Proposta inicial da distribuição de autoria e revisão das issues #78 a #111 |
| 1.1 | 19/11/2026 | Isadora Yasmim da Silva | Distribuição confirmada pelo grupo, revisores registrados nas issues e situação das pendências atualizada |
| 1.2 | 19/11/2026 | Isadora Yasmim da Silva | Servidor do Discord criado; convite à docente aguardando o usuário dela |
