# Protótipo de telas

**Projeto:** Sistema Web de Feedback e Gestão de Competências  
**Disciplina:** Domínios de Software (INF0296, 2026/2) · 1ª Etapa: Levantamento de Requisitos  
**Issue:** #50 · **Versão:** 1.2 · **Data:** 18/11/2026  
**Responsáveis:** Júlia de Souza Nascimento e Verônica Ribeiro Oliveira Palmeira  
**Ferramenta:** Figma  
**Base:** [Lista Geral de Requisitos](../Lista_Geral_Requisitos.md) (#45) e [Diagrama de Casos de Uso](../modelagem/casos-de-uso/Diagrama_Casos_de_Uso.md) (#47)

## Histórico de revisões

| Versão | Data | Descrição | Autora |
|---|---|---|---|
| 1.0 | 17/11/2026 | Registro do link e do escopo do protótipo | Júlia de Souza Nascimento |
| 1.1 | 17/11/2026 | Revisão final (#55): quantidade de telas e fluxos, com a numeração `T-xx` da matriz | Verônica Ribeiro Oliveira Palmeira |
| 1.2 | 18/11/2026 | Cabeçalho padronizado; nova seção "Papel no processo e limitações conhecidas" | Verônica Ribeiro Oliveira Palmeira |

## Acesso

[Abrir o protótipo no Figma](https://www.figma.com/design/yiyjqLFpIp838MAi9x0EW4/Dom%C3%ADnios-de-Software-2026-2?node-id=6-3)

O link abre o arquivo **Domínios de Software 2026-2** no nó indicado. Os detalhes visuais e a navegação entre telas devem ser consultados diretamente no Figma, que é a fonte do protótipo.

## Escopo

O protótipo representa os principais fluxos previstos para o sistema:

- login e consentimento relacionado à LGPD;
- dashboard do colaborador, com evolução, gráficos e tendências;
- emissão de feedback por chefia, pares e avaliação 360°, incluindo modalidades formais, informais, positivas e construtivas;
- resposta a questionários de avaliação;
- relatório consolidado com proteção do anonimato;
- plano de ação, metas de desenvolvimento e histórico de feedbacks;
- administração de ciclos e questionários pelo RH;
- ao menos uma tela em versão mobile.

Este artefato documenta o acesso e o escopo do protótipo; não substitui a especificação de requisitos nem representa uma implementação funcional do sistema.

## Telas

O protótipo tem **51 telas**: 47 na versão web e 4 na versão para celular. A [matriz de rastreabilidade](../Matriz_Rastreabilidade.md) (#49, seção 4) numera as telas de `T-01` a `T-51` e liga cada uma aos casos de uso e aos requisitos que ela atende.

| Fluxo do escopo | Telas |
|---|---|
| Login, verificação em duas etapas e aviso de tratamento de dados (LGPD) | T-01 a T-04 |
| Painel do colaborador, com evolução, gráficos e tabela acessível | T-05 a T-07 |
| Emissão de feedback formal e informal, positivo e construtivo, com validações e alertas | T-08 a T-13 |
| Resposta a avaliações nos modos confidencial e anônimo | T-14 a T-18 |
| Resultado consolidado do ciclo, com mínimo de respondentes | T-19 |
| Plano de ação, metas, feedbacks recebidos e enviados, réplica e histórico | T-20 a T-27 |
| Planejamento, acompanhamento e encerramento de ciclos, questionários e moderação (RH e gestor) | T-28 a T-38 |
| Painéis da equipe e da organização | T-39, T-40 |
| Direitos do titular, registro de fato, pedido de feedback, importação de cadastro, acessibilidade, agendamento de sessão e notificações | T-41 a T-47 |
| Versão para celular: painel e emissão de feedback | T-48 a T-51 |

Os casos de uso sem tela e as anotações do Figma que citam requisitos diferentes dos da lista geral estão registrados na matriz (seções 4.1 e 4.2). Nessas anotações, vale a correção da matriz.

## Papel no processo e limitações conhecidas

O protótipo é a técnica de validação e de elicitação complementar do [processo de requisitos](../Processo_Requisitos.md) (seções 2.4 e 3, prefixo `RT`). Ele mostra como os requisitos da lista geral aparecem nas telas, nos fluxos dos casos de uso. Nenhum requisito novo surgiu na prototipação, por isso não há candidatos `RT` na lista geral.

| Limitação | Situação | Onde está registrada |
|---|---|---|
| As anotações de 9 telas no Figma citam requisitos diferentes dos da lista geral | A matriz traz a correção de cada uma. Vale a matriz até as anotações serem corrigidas no Figma | [Matriz](../Matriz_Rastreabilidade.md), seção 4.2 |
| RF-005, RF-006 (competências do cargo e específicas) e RF-062 (política de retenção), de prioridade Must, ainda não têm tela | Os requisitos estão rastreados pelos casos de uso UC-03, UC-04 e UC-28 e pelas entidades do modelo ER | [Matriz](../Matriz_Rastreabilidade.md), seções 7 e 8 |

