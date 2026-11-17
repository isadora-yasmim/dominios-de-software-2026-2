# Especificação Suplementar

**Projeto:** Sistema de Gestão de Competências (módulo de Feedback)
**Disciplina:** Domínios de Software (2026/2) · 1ª Etapa: Levantamento de Requisitos
**Issue:** #51 · **Versão:** 1.0 · **Data:** 17/11/2026
**Responsável:** Verônica Ribeiro Oliveira Palmeira
**Base:** [Lista Geral de Requisitos](Lista_Geral_Requisitos.md), versão 1.0 (#45)

## Histórico de revisões

| Versão | Data | Descrição | Autora |
|---|---|---|---|
| 1.0 | 17/11/2026 | Versão inicial: requisitos não funcionais e restrições organizados pela ISO/IEC 25010:2023, com critérios de aceitação e métodos de verificação | Verônica Ribeiro Oliveira Palmeira |

---

## Sumário

1. [Introdução](#1-introdução)
2. [Modelo de qualidade](#2-modelo-de-qualidade)
3. [Adequação funcional](#3-adequação-funcional)
4. [Eficiência de desempenho](#4-eficiência-de-desempenho)
5. [Compatibilidade](#5-compatibilidade)
6. [Capacidade de interação (usabilidade e acessibilidade)](#6-capacidade-de-interação-usabilidade-e-acessibilidade)
7. [Confiabilidade](#7-confiabilidade)
8. [Segurança](#8-segurança)
9. [Manutenibilidade](#9-manutenibilidade)
10. [Flexibilidade (portabilidade)](#10-flexibilidade-portabilidade)
11. [Proteção (safety)](#11-proteção-safety)
12. [Restrições legais e de implementação](#12-restrições-legais-e-de-implementação)
13. [Interfaces](#13-interfaces)
14. [Regras de negócio relacionadas](#14-regras-de-negócio-relacionadas)
15. [Decisões desta especificação](#15-decisões-desta-especificação)
16. [Rastreabilidade e cobertura](#16-rastreabilidade-e-cobertura)
17. [Referências](#17-referências)

---

## 1. Introdução

### 1.1 Objetivo

Este documento reúne os requisitos que não cabem nos casos de uso: atributos de qualidade, restrições de projeto, interfaces e questões legais. É o artefato que Larman chama de Especificação Suplementar (cap. 7). Para cada requisito não funcional, o documento define um **critério de aceitação** mensurável e o **método de verificação**, para que ele possa ser testado ou inspecionado sem depender de interpretação.

### 1.2 Escopo

- **Requisitos especificados:** os 36 requisitos não funcionais da lista geral, de RNF-001 a RNF-036, com os mesmos identificadores, textos e prioridades.
- **Requisitos citados:** requisitos funcionais (RF) e regras de negócio (RN) que se ligam a um atributo de qualidade aparecem como "relacionados". Eles não são repetidos aqui, porque já estão na lista geral e serão detalhados nos casos de uso.
- **Fora deste documento:** o comportamento funcional (casos de uso, #47 e #48), os dados (modelo ER, #52) e os termos (glossário, #53).

Este documento não cria requisitos novos. Quando a lista geral deixou um valor em aberto, por exemplo o número de tentativas de login ou o volume de usuários, a decisão foi tomada aqui com base em norma ou nas fontes do projeto e está registrada na seção 15.

### 1.3 Relação com os outros artefatos

| Artefato | Relação |
|---|---|
| [Lista Geral de Requisitos](Lista_Geral_Requisitos.md) (#45) | Fonte dos identificadores, textos, origens e prioridades. Os pontos a validar da lista (seção 9) continuam valendo, em especial o P-10, sobre as metas numéricas |
| [Pesquisa documental](elicitacao/pesquisa-documental/Pesquisa_Documental.md) (#33) | Fonte das obrigações legais e normas técnicas e da adaptação da ISO/IEC 25010:2023 ao sistema |
| Documento Visão (#46) | Resume os atributos de qualidade mais importantes para os interessados |
| Casos de uso (#47 e #48) | Descrevem o comportamento funcional. Os requisitos especiais de cada caso de uso devem apontar para os RNF deste documento |
| Modelo ER (#52) | Deve refletir as decisões de armazenamento da seção 8: vínculo pseudonimizado do emissor e controle de participação separado |
| Especificação IEEE 830 (#54) | Usa este documento como fonte da sua seção de requisitos não funcionais |
| Matriz de rastreabilidade (#49) | Usa a seção 16 para ligar cada RNF à característica de qualidade e ao método de verificação |

### 1.4 Como ler as tabelas

| Coluna | Conteúdo |
|---|---|
| **ID** | Identificador definitivo da lista geral |
| **Requisito** | Texto da lista geral, sem alteração |
| **Subcaracterística** | Subcaracterística da ISO/IEC 25010:2023 que o requisito atende |
| **Critério de aceitação** | Condição mensurável que precisa ser verdadeira para o requisito ser considerado atendido |
| **Verificação** | Método de verificação: **T** teste, **I** inspeção, **A** análise, **D** demonstração |
| **Prior.** | Prioridade MoSCoW da lista geral |

**Requisitos com mais de uma característica.** Alguns RNF atendem a duas características, por exemplo RNF-012 (confiabilidade e capacidade de interação). Cada um aparece uma única vez, na seção da característica principal, e é citado nas demais.

**Prioridade Won't.** Os requisitos Won't ficam registrados com critério de aceitação, para orientar a versão futura, mas não são verificados nesta versão.

**Termos em português.** As traduções dos nomes da ISO/IEC 25010:2023 seguem a [pesquisa documental](elicitacao/pesquisa-documental/Pesquisa_Documental.md) (seção 4), com o termo em inglês entre parênteses quando ajuda a identificar o conceito.

---

## 2. Modelo de qualidade

### 2.1 ISO/IEC 25010:2023

Os requisitos estão organizados pela ISO/IEC 25010:2023, a edição vigente do modelo de qualidade de produto. Ela substituiu a edição de 2011 e trouxe três mudanças que afetam esta especificação (pesquisa documental, seção 4.1):

- **Usabilidade** passou a se chamar **capacidade de interação** (*interaction capability*) e ganhou as subcaracterísticas inclusividade, assistência ao usuário e autodescritividade.
- **Portabilidade** passou a se chamar **flexibilidade** (*flexibility*) e ganhou a subcaracterística escalabilidade.
- Surgiu a característica **proteção** (*safety*), que trata de evitar danos a pessoas, ao negócio ou ao ambiente.

### 2.2 Correspondência entre a issue, a norma e o livro

A checklist da issue #51 usa nomes da edição de 2011 em alguns itens. Larman organiza a especificação suplementar pelo modelo FURPS+. A tabela mostra onde cada item foi tratado.

| Item da issue #51 | ISO/IEC 25010:2023 | FURPS+ (Larman) | Seção | RNF |
|---|---|---|---|---|
| Adequação funcional | Adequação funcional | Funcionalidade | 3 | RNF-007 |
| Eficiência de desempenho | Eficiência de desempenho | Desempenho (*Performance*) | 4 | RNF-008, RNF-009 |
| Compatibilidade | Compatibilidade | Interfaces (+) | 5 | RNF-025 |
| Usabilidade / interação (inclui acessibilidade) | Capacidade de interação | Usabilidade | 6 | RNF-013 a RNF-023 |
| Confiabilidade | Confiabilidade | Confiabilidade | 7 | RNF-010 a RNF-012 |
| Segurança (confidencialidade, anonimato, criptografia, LGPD) | Segurança | Funcionalidade (segurança) | 8 | RNF-001 a RNF-006 |
| Manutenibilidade | Manutenibilidade | Suportabilidade | 9 | RNF-026 |
| Portabilidade / flexibilidade (web → mobile) | Flexibilidade | Suportabilidade (adaptabilidade) | 10 | RNF-027 a RNF-029 |
| Não consta na checklist | Proteção (*safety*) | — | 11 | RNF-024 |
| Restrições legais e de implementação | Fora do modelo de qualidade | Implementação (+) e Legal (+) | 12 | RNF-030 a RNF-036 |

A característica **proteção** não está na checklist porque não existia na edição de 2011. Ela foi mantida porque a lista geral tem um requisito classificado nela (RNF-024).

### 2.3 Distribuição dos requisitos

| Característica | Must | Should | Could | Won't | Total |
|---|---|---|---|---|---|
| Adequação funcional | 0 | 1 | 0 | 0 | 1 |
| Eficiência de desempenho | 0 | 2 | 0 | 0 | 2 |
| Compatibilidade | 0 | 0 | 0 | 1 | 1 |
| Capacidade de interação | 8 | 3 | 0 | 0 | 11 |
| Confiabilidade | 0 | 3 | 0 | 0 | 3 |
| Segurança | 4 | 2 | 0 | 0 | 6 |
| Manutenibilidade | 0 | 1 | 0 | 0 | 1 |
| Flexibilidade | 2 | 1 | 0 | 0 | 3 |
| Proteção | 0 | 0 | 1 | 0 | 1 |
| Restrições | 4 | 1 | 0 | 2 | 7 |
| **Total** | **18** | **14** | **1** | **3** | **36** |

---

## 3. Adequação funcional

**Por que importa.** O enunciado pede uma "análise robusta" com tendências e números. Um gráfico com poucas respostas, sem informar quantas, leva a conclusões erradas sobre uma pessoa. Por isso a correção dos números exibidos é tratada como requisito de qualidade.

| ID | Requisito | Subcaracterística | Critério de aceitação | Verificação | Prior. |
|---|---|---|---|---|---|
| RNF-007 | Toda média, tendência ou gráfico exibido deve informar o período e o número de respostas que o compõem. | Correção funcional; também capacidade de interação (autodescritividade) | 1. Todo componente que exibe média, tendência ou gráfico mostra, junto ao valor, a data inicial, a data final e o número de respostas (n). 2. Com um conjunto de dados de teste de resultado conhecido, os valores exibidos são iguais aos calculados à mão | I (todas as telas de painel e consolidação); T (conjunto de dados de teste) | Should |

**Relacionados:** RF-032 (consolidação), RF-033 (comparação com a autoavaliação), RF-049 e RF-050 (painéis), RN-005 (mínimo de respondentes), RN-008 (indicadores como apoio à decisão, com os critérios de cálculo exibidos).

---

## 4. Eficiência de desempenho

**Por que importa.** O uso se concentra no encerramento dos ciclos formais, quando a maior parte dos colaboradores responde na mesma semana (pesquisa documental, seção 4.2). Hoje a consolidação de um ciclo leva cerca de uma semana (Q02).

### 4.1 Cenário de referência

As metas desta seção e da seção 10 são medidas no cenário abaixo (decisões DS-01 a DS-03).

| Parâmetro | Valor | Fonte |
|---|---|---|
| Colaboradores cadastrados | 500 | Limite superior do porte informado nos dois questionários, de 100 a 499 funcionários (Q01 e Q02). A secretaria da E02 tem 330 pessoas na rede (E02 §1) |
| Usuários simultâneos no pico | 500 | Pior caso: todos os colaboradores usando o sistema ao mesmo tempo. As fontes não informam a distribuição dos acessos ao longo do dia |
| Operações do pico | Abrir o painel, responder a uma avaliação, registrar e enviar um feedback, consultar o histórico | Telas citadas no RNF-008 e fluxo de resposta do ciclo (RF-027) |
| Rede | Perfil de limitação de rede 4G das ferramentas de desenvolvedor do navegador, o mesmo em todas as medições | RNF-008 ("em conexão 4G") |

### 4.2 Requisitos

| ID | Requisito | Subcaracterística | Critério de aceitação | Verificação | Prior. |
|---|---|---|---|---|---|
| RNF-008 | As telas principais (painel, formulário de feedback e histórico) devem carregar em até 3 s e o envio de um feedback deve ser confirmado em até 2 s, no percentil 95, em conexão 4G. | Comportamento temporal | 1. Tempo entre a solicitação da tela e a exibição do conteúdo principal pronto para uso: até 3 s no percentil 95, para cada uma das três telas. 2. Tempo entre o comando de envio e a confirmação na tela: até 2 s no percentil 95. 3. Cada percentil é calculado sobre pelo menos 100 medições da operação, no cenário de referência (4.1) | T (teste de desempenho com carga) | Should |
| RNF-009 | O sistema deve suportar o pico de um ciclo formal, quando a maior parte dos colaboradores responde na mesma semana, sem descumprir RNF-008. | Capacidade | Com 500 usuários virtuais simultâneos executando as operações do pico: 1. as metas do RNF-008 continuam atendidas; 2. nenhuma requisição termina em erro do servidor | T (teste de carga) | Should |

**Relacionados:** RF-032 (consolidação automática ao encerrar o ciclo), RNF-029 (escalabilidade além do cenário de referência).

---

## 5. Compatibilidade

**Por que importa.** A PO aceitou a importação por planilha ou o cadastro manual no lugar da integração com sistemas de RH (E01 §30). Por isso, nesta versão, a interoperabilidade se dá por arquivos em formato aberto, e a integração por API fica para depois.

| ID | Requisito | Subcaracterística | Critério de aceitação | Verificação | Prior. |
|---|---|---|---|---|---|
| RNF-025 | O sistema deve oferecer integração com sistemas de RH e de folha de pagamento por API documentada. | Interoperabilidade | Para a versão futura: um sistema de RH consegue criar e atualizar colaboradores, cargos, equipes e hierarquia usando apenas a documentação publicada da API | D (versão futura) | Won't |

**Interoperabilidade nesta versão.** É atendida por requisitos funcionais, com os formatos definidos na seção 13: importação de colaboradores por CSV (RF-002) e exportação dos dados do titular em JSON ou CSV (RF-058).

**Coexistência.** O sistema é usado no navegador, ao lado de outros programas do usuário. Os navegadores suportados estão definidos no RNF-030 (seção 12).

---

## 6. Capacidade de interação (usabilidade e acessibilidade)

**Por que importa.** "Gestores não sabem dar feedback" foi o problema citado nos dois questionários, e dar feedback "dá trabalho" (E01 §9). Se o registro for demorado, o feedback deixa de ser dado. A acessibilidade é obrigação legal (Lei Brasileira de Inclusão, art. 63) e a ABNT NBR 17225:2025 é a norma técnica brasileira que a detalha, com base nas WCAG 2.2.

### 6.1 Operabilidade, aprendizagem e proteção contra erro

| ID | Requisito | Subcaracterística | Critério de aceitação | Verificação | Prior. |
|---|---|---|---|---|---|
| RNF-013 | O registro de um feedback informal deve caber em uma única tela, com apenas os campos obrigatórios de RN-002. | Operabilidade | 1. O formulário de feedback informal fica em uma única página, sem etapas nem navegação para outra página até o envio. 2. Só os campos de RN-002 são obrigatórios. Os demais podem ficar em branco | I | Should |
| RNF-014 | Um avaliador deve conseguir concluir a avaliação de um colega em até 20 minutos. | Operabilidade | Em teste de usabilidade com pelo menos 5 participantes que não conheçam o sistema, cada participante conclui a avaliação de um colega com o questionário padrão da organização (RF-008) em até 20 minutos, contados da abertura da avaliação até a confirmação do envio | T (teste de usabilidade) | Should |
| RNF-015 | Os formulários devem validar os campos com mensagens claras e pedir confirmação antes de ações irreversíveis, como enviar um feedback ou encerrar um ciclo. | Proteção contra erro do usuário | 1. Cada erro de preenchimento é indicado junto ao campo, com texto que diz o que corrigir. 2. Enviar feedback, enviar avaliação e encerrar ciclo pedem confirmação explícita e informam a consequência, por exemplo que o feedback enviado não pode ser excluído (RN-003). 3. Atende ao critério 3.3.4 das WCAG 2.2 (prevenção de erros) | I; T | Should |
| RNF-016 | A interface, as mensagens, as orientações e os modelos de perguntas devem estar em português do Brasil. | Aprendizagem | 1. Todos os textos da interface, mensagens, e-mails, orientações e modelos de perguntas estão em português do Brasil. 2. Datas no formato dd/mm/aaaa e números com vírgula decimal | I | Must |

**Relacionados:** RNF-012 (rascunho automático, seção 7), RF-017 e RF-018 (orientações ao emissor), RF-019 (aviso de quem verá o conteúdo).

### 6.2 Inclusividade (acessibilidade)

O RNF-017 é o requisito geral. Os RNF-018 a RNF-023 detalham os critérios das WCAG 2.2 mais relevantes para um sistema feito de formulários, painéis com gráficos e uso em telas pequenas (pesquisa documental, seção 6.3). Ferramentas automáticas encontram só parte das falhas de acessibilidade, por isso os critérios combinam verificação automática, inspeção manual e teste com tecnologia assistiva.

| ID | Requisito | Subcaracterística | Critério de aceitação | Verificação | Prior. |
|---|---|---|---|---|---|
| RNF-017 | A interface web deve atender aos requisitos da ABNT NBR 17225:2025 e aos critérios de nível A e AA das WCAG 2.2. | Inclusividade | 1. Nenhuma falha nos critérios de sucesso de nível A e AA das WCAG 2.2. 2. Todos os requisitos (não as recomendações) da ABNT NBR 17225:2025 atendidos. 3. Resultado registrado na declaração de acessibilidade (RF-065) | A (ferramenta automática); I (lista de verificação da NBR 17225); T (leitor de tela) | Must |
| RNF-018 | Todas as funcionalidades devem ser operáveis por teclado, com foco sempre visível e não encoberto por outros elementos. | Inclusividade; operabilidade | Critérios WCAG 2.1.1 (teclado), 2.4.7 (foco visível) e 2.4.11 (foco não encoberto, mínimo): é possível concluir cada caso de uso só com o teclado, e o elemento em foco fica visível em todos os passos | T (navegação só por teclado) | Must |
| RNF-019 | O contraste deve ser de no mínimo 4,5:1 para texto normal e 3:1 para texto grande e componentes de interface, e a cor não pode ser o único meio de transmitir informação. | Inclusividade | Critérios WCAG 1.4.3, 1.4.11 e 1.4.1: razões de contraste medidas atingem os mínimos. Status de metas e linhas de gráficos usam também texto, ícone ou padrão, além da cor | A (medição de contraste); I | Must |
| RNF-020 | Os gráficos de evolução e de indicadores devem ter alternativa textual equivalente, com resumo e tabela de dados. | Inclusividade | Critério WCAG 1.1.1: todo gráfico tem um resumo em texto e uma tabela com os mesmos dados, ambos acessíveis por leitor de tela | I; T (leitor de tela) | Must |
| RNF-021 | Os formulários devem ter rótulos e instruções, identificar o erro e sugerir a correção, e não pedir de novo informação já fornecida no mesmo processo. | Inclusividade; proteção contra erro do usuário | Critérios WCAG 3.3.1, 3.3.2, 3.3.3 e 3.3.7: todo campo tem rótulo; todo erro é descrito em texto com a sugestão de correção; nenhum dado informado em um passo é pedido de novo no mesmo processo | I; T | Must |
| RNF-022 | O login não pode depender de teste cognitivo sem alternativa e deve permitir colar a senha e usar gerenciadores de senha. | Inclusividade; também segurança (autenticidade) | Critério WCAG 3.3.8: o campo de senha aceita colar e preenchimento por gerenciador de senha; nenhuma etapa do login exige resolver enigma, lembrar caracteres ou transcrever código sem alternativa | T | Must |
| RNF-023 | As páginas devem usar HTML semântico (títulos, regiões e rótulos), declarar o idioma pt-BR, aceitar texto ampliado em 200% sem perda de conteúdo e funcionar com leitores de tela. | Inclusividade | Critérios WCAG 1.3.1, 1.4.4, 3.1.1 e 4.1.2: idioma declarado como pt-BR em todas as páginas; com o texto ampliado a 200%, nenhum conteúdo ou função se perde; os casos de uso principais podem ser concluídos com leitor de tela | A; T (leitor de tela e ampliação) | Must |

**Relacionados:** RF-065 (símbolo e declaração de acessibilidade), RNF-027 (responsividade, seção 10), RNF-036 (acessibilidade do aplicativo futuro, seção 12).

---

## 7. Confiabilidade

**Por que importa.** A PO relatou um sistema que descartava o cadastro incompleto (E01 §33). Perder uma resposta escrita com cuidado desestimula o feedback, que já é pouco frequente. Os prazos dos ciclos também não podem ser comprometidos por indisponibilidade.

| ID | Requisito | Subcaracterística | Critério de aceitação | Verificação | Prior. |
|---|---|---|---|---|---|
| RNF-010 | O sistema deve ter disponibilidade mínima de 99,5% ao mês, com janelas de manutenção comunicadas com antecedência e fora dos prazos dos ciclos de avaliação. | Disponibilidade | 1. Disponibilidade medida por monitoramento externo, que verifica a cada minuto se o login e a API respondem: no mínimo 99,5% dos minutos do mês, ou seja, até 3 h 36 min de indisponibilidade em um mês de 30 dias, incluindo manutenções. 2. Nenhuma janela de manutenção coincide com o período de resposta de um ciclo formal aberto. 3. Cada janela é anunciada no sistema antes de começar, com data, hora e duração, na antecedência definida em contrato (DS-11) | A (relatório mensal do monitoramento); I (calendário de manutenções × ciclos) | Should |
| RNF-011 | O sistema deve ter backups criptografados diários, com perda máxima de 24 h de dados (RPO), restauração em até 4 h (RTO) e testes periódicos de restauração. | Recuperabilidade | 1. Existe pelo menos um backup completo a cada 24 h, criptografado como define o RNF-004. 2. No teste de restauração, o sistema volta a operar em até 4 h, com os dados do último backup. 3. Um teste de restauração é feito antes da abertura de cada ciclo formal (DS-08). 4. Os backups seguem a política de retenção (DS-09) | T (restauração cronometrada); I (registros de backup) | Should |
| RNF-012 | Respostas a feedbacks e questionários devem ser salvas automaticamente como rascunho, para que nada se perca em caso de queda de conexão, sessão expirada ou campos obrigatórios ainda em branco. | Tolerância a falhas; também capacidade de interação (proteção contra erro do usuário) | 1. O rascunho é salvo sem ação do usuário a cada campo preenchido. 2. Depois de queda de conexão, de expiração da sessão (RNF-006) ou de fechamento do navegador, ao reabrir o formulário o usuário encontra todos os campos já concluídos. 3. Campos obrigatórios em branco não impedem salvar o rascunho, só o envio. 4. O rascunho é visível apenas para o autor (RNF-002) | T (os três cenários de falha) | Should |

**Ausência de falhas (*faultlessness*).** Nenhum RNF da lista geral trata dessa subcaracterística isoladamente. Ela é coberta pelos testes de cada requisito.

---

## 8. Segurança

**Por que importa.** A confidencialidade é o ponto mais sensível do projeto e aparece em todas as fontes (pesquisa documental, seção 3.5). A disposição a ser sincero com o gestor identificado teve média de 1,5 em 5 nos questionários. O conteúdo de um feedback é dado pessoal de duas pessoas ao mesmo tempo: de quem recebe e de quem emite. A LGPD exige medidas de segurança desde a concepção (art. 46, §2º).

### 8.1 Controle de acesso

A matriz abaixo detalha o RNF-001 e a RN-004. A lista do RNF-001 é fechada: perfis que não aparecem nela, como o administrador, não veem o conteúdo de feedbacks.

| Perfil | Feedbacks e avaliações de um colaborador | Identidade do emissor confidencial | Identidade do emissor anônimo | Resultados agregados |
|---|---|---|---|---|
| Colaborador (receptor) | Os seus | Não | Não | Os seus, respeitado o mínimo de RN-005 |
| Emissor | Só o conteúdo que ele escreveu | — | — | Não |
| Gestor direto | Os da sua equipe | Não | Não | Os da sua equipe, respeitado o mínimo de RN-005 |
| RH | Os de toda a organização | Sim, com registro na trilha de auditoria (RNF-005), exceto nas avaliações em que ele próprio é o avaliado (RN-004) | Não | Os da organização, respeitado o mínimo de RN-005 |
| Diretoria | Não | Não | Não | Os da organização, respeitado o mínimo de RN-005 (ponto a validar P-02 da lista) |
| Administrador | Não | Não | Não | Não |

Fatos registrados e ainda não vinculados a um feedback são visíveis só para quem os registrou (RF-011). Rascunhos são visíveis só para o autor (RNF-012).

### 8.2 Requisitos

| ID | Requisito | Subcaracterística | Critério de aceitação | Verificação | Prior. |
|---|---|---|---|---|---|
| RNF-001 | Um feedback e o resultado de avaliação de um colaborador só podem ser vistos pelo próprio colaborador, pelo emissor (apenas o conteúdo que ele escreveu), pelo gestor direto do colaborador e pelo RH. A diretoria da organização vê apenas indicadores agregados, conforme RN-005. | Confidencialidade | 1. Para cada perfil da matriz 8.1, as consultas permitidas retornam os dados e as demais são negadas. 2. A negação vale também para chamadas diretas à API (RNF-028), inclusive com identificadores de registros de outro colaborador | T (testes de autorização por perfil, pela interface e pela API) | Must |
| RNF-002 | Todo feedback novo deve ficar visível apenas ao público mínimo de RNF-001. A visibilidade é definida no envio e só pode ser ampliada por nova ação explícita do emissor. | Confidencialidade | 1. Um feedback recém-criado, sem nenhuma configuração adicional, fica visível só aos perfis da matriz 8.1. 2. Nenhuma opção de visibilidade vem marcada por padrão. 3. Ampliar a visibilidade exige ação do emissor, registrada na trilha de auditoria | T; I | Must |
| RNF-003 | Nos feedbacks e avaliações em modo confidencial, o vínculo entre emissor e resposta deve ser armazenado separado do conteúdo (pseudonimização), com acesso restrito ao RH e registrado na trilha de auditoria. | Confidencialidade; responsabilização | 1. O conteúdo da resposta é armazenado sem o identificador do emissor. 2. O vínculo emissor–resposta fica em armazenamento separado, com controle de acesso próprio. 3. Só o perfil RH consegue consultar o vínculo, e cada consulta gera registro na trilha de auditoria. 4. A consulta é negada quando o usuário do RH é o avaliado (RN-004) | I (modelo de dados, #52); T | Should |
| RNF-004 | Dados pessoais e conteúdo de feedback devem ser criptografados em trânsito (TLS 1.2 ou superior) e em repouso. | Confidencialidade; integridade | 1. Toda comunicação com o sistema usa TLS 1.2 ou superior; conexões sem TLS ou com versões anteriores são recusadas. 2. Banco de dados, arquivos e backups são armazenados criptografados com algoritmo simétrico padronizado, como o AES | A (varredura da configuração TLS); I (configuração do armazenamento) | Must |
| RNF-005 | O sistema deve manter trilha de auditoria inalterável dos acessos e das alterações a dados pessoais e feedbacks (quem, quando, o quê e de onde), incluindo toda consulta à identidade de emissores confidenciais. | Responsabilização; não repúdio | 1. Cada registro contém usuário, data e hora, ação, objeto afetado e endereço de origem. 2. Nenhum perfil, inclusive o administrador, consegue alterar ou excluir registros pela aplicação. 3. Uma alteração feita fora da aplicação, direto no armazenamento, é detectável, por exemplo por encadeamento de resumos criptográficos (*hash*). 4. O prazo de guarda segue a política de retenção (RF-062) e, se o sistema for operado como serviço, o RNF-032 | T; I | Must |
| RNF-006 | O sistema deve exigir autenticação em dois fatores para RH e administradores, bloquear o acesso após tentativas sucessivas de login sem sucesso e encerrar a sessão após um período de inatividade. | Autenticidade; resistência | 1. Usuários com perfil RH ou administrador só acessam com dois fatores de autenticação. 2. Após cada falha de login, o sistema impõe uma espera crescente, de 30 s até 1 h, e desativa o autenticador ao atingir 100 falhas consecutivas na conta; ele só volta a funcionar depois de ser vinculado de novo à conta, por redefinição (DS-06). 3. Um login bem-sucedido zera a contagem de falhas. 4. A sessão é encerrada após 1 h sem atividade e após 24 h de duração total, para todos os perfis (DS-05) | T | Should |

**Relacionados:** RNF-022 (login acessível, seção 6.2), RNF-032 (guarda dos registros de acesso, seção 12), RF-019 (aviso ao emissor sobre quem verá o conteúdo), RF-063 (gestão de incidentes).

### 8.3 Confidencialidade e anonimato: requisitos de armazenamento

Os modos de identificação do emissor são regras de negócio (RN-004 e RN-005, na lista geral). Esta seção define o que eles exigem do armazenamento e da exibição, para que possam ser verificados. O modelo ER (#52) deve refletir essas condições.

| Regra | Condição verificável | Verificação |
|---|---|---|
| RN-004, modo identificado | O receptor vê o nome do emissor junto ao feedback | T |
| RN-004, modo confidencial | Vale o RNF-003: conteúdo sem o identificador do emissor, vínculo separado, consulta só pelo RH, com auditoria | I; T |
| RN-004, modo anônimo | 1. A resposta é armazenada sem identificador do emissor e sem pseudônimo que permita chegar a ele. 2. O controle de quem já respondeu, usado pelo RF-029, fica em registro separado, que guarda só "respondeu" ou "não respondeu" por convidado, sem ligação com o conteúdo. 3. Os dois registros não compartilham dado que permita ligá-los, como o horário exato do envio ou o identificador da sessão (DS-12) | I (modelo de dados); A (tentativa de reidentificação com os dados armazenados) |
| RN-004, rótulo | A palavra "anônimo" só aparece na interface quando o modo é anônimo. Nos demais modos, o aviso do RF-019 diz quem pode ver a identidade | I |
| RN-005, mínimo de respondentes | Com menos respondentes do que o mínimo configurado (padrão 3) em uma fonte confidencial ou anônima, o resultado dessa fonte não é exibido isoladamente: é agrupado em outra categoria ou omitido | T (conjunto de dados com 2 e com 3 respondentes) |

### 8.4 LGPD

A conformidade com a LGPD (RNF-031) é atendida pelo conjunto de requisitos listados na seção 12.2. Os requisitos desta seção 8 são as medidas técnicas de segurança do art. 46. Os direitos do titular (art. 18) são requisitos funcionais (RF-053 a RF-061) e serão detalhados nos casos de uso.

---

## 9. Manutenibilidade

**Por que importa.** As competências mudam por cargo, e a PO quer poder mudar perguntas e parâmetros (E01 §15, §29). Se cada mudança exigir programação, o sistema não acompanha a organização.

| ID | Requisito | Subcaracterística | Critério de aceitação | Verificação | Prior. |
|---|---|---|---|---|---|
| RNF-026 | Competências, questionários, modalidades de feedback e ciclos devem ser parametrizáveis pelo administrador, sem alteração de código. | Modificabilidade; também flexibilidade (adaptabilidade) | O administrador cria, altera e desativa competências, questionários, modalidades e parâmetros de ciclo pela interface do sistema, e a mudança passa a valer sem nova versão do software nem intervenção técnica | D | Should |

**Modularidade e reusabilidade.** São atendidas pelo RNF-028 (API independente da interface), especificado na seção 10 porque a sua finalidade principal é a versão móvel.

---

## 10. Flexibilidade (portabilidade)

**Por que importa.** O enunciado pede plataforma web com "perspectiva futura de rodar além do computador em dispositivos móveis". A pesquisa documental concluiu que a interface responsiva e a API separada da interface são necessárias desde a primeira versão, e que o aplicativo nativo pode ficar para depois (seção 6.4).

| ID | Requisito | Subcaracterística | Critério de aceitação | Verificação | Prior. |
|---|---|---|---|---|---|
| RNF-027 | A interface deve ser responsiva: sem rolagem horizontal a 320 px de largura, funcional em retrato e paisagem e com alvos de toque de no mínimo 24 × 24 px CSS. | Adaptabilidade; também capacidade de interação (operabilidade) | Critérios WCAG 1.4.10, 1.3.4 e 2.5.8: 1. a 320 px CSS de largura, nenhuma tela exige rolagem horizontal, salvo tabelas de dados e gráficos; 2. todas as telas funcionam em retrato e em paisagem; 3. todo alvo de toque mede pelo menos 24 × 24 px CSS ou tem o espaçamento equivalente previsto no critério 2.5.8 | T (navegadores da seção 12, em celular e computador) | Must |
| RNF-028 | O back-end deve expor todas as funcionalidades por uma API independente da interface web, para que o futuro aplicativo móvel reutilize as mesmas regras de negócio. | Adaptabilidade; também manutenibilidade (modularidade, reusabilidade) | 1. Toda função disponível na interface web pode ser executada pela API. 2. A interface web acessa os dados só pela API e não contém regra de negócio que a API não aplique. 3. A API tem documentação publicada em formato padronizado, como a especificação OpenAPI | I (arquitetura); A (cada caso de uso tem as operações de API correspondentes) | Must |
| RNF-029 | A arquitetura deve permitir aumentar o número de colaboradores atendidos sem reescrever o sistema. | Escalabilidade | Com o dobro do cenário de referência (1.000 colaboradores e 1.000 usuários simultâneos), as metas do RNF-008 são atendidas depois de ampliar apenas recursos de infraestrutura, sem alteração do código (DS-04) | T (teste de carga) | Should |

**Relacionados:** RNF-035 (aplicativo móvel futuro, seção 12), RN-010 (uma organização por instalação: a escalabilidade é em número de colaboradores, não de organizações).

---

## 11. Proteção (safety)

**Por que importa.** Um feedback escrito com agressividade causa dano psicológico a quem recebe e pode gerar responsabilidade para o empregador (CLT, arts. 223-B e 223-C). A PO citou feedbacks construtivos dados com "uma dose de agressividade" (E01 §20).

| ID | Requisito | Subcaracterística | Critério de aceitação | Verificação | Prior. |
|---|---|---|---|---|---|
| RNF-024 | Antes do envio, o sistema deve sinalizar ao emissor termos potencialmente ofensivos ou discriminatórios e sugerir a revisão, sem bloquear o envio. | Alerta de perigo | 1. Se o texto contiver termo de uma lista mantida pelo administrador, o sistema mostra um alerta antes do envio, indicando o trecho e sugerindo revisão (DS-13). 2. O emissor pode revisar ou enviar mesmo assim. 3. Nenhum envio é bloqueado pelo alerta | T (textos com e sem termos da lista) | Could |

**Relacionados:** RF-017 e RF-018 (orientações ao emissor), RN-001 (feedback baseado em fatos), RN-014 (critérios não discriminatórios).

---

## 12. Restrições legais e de implementação

### 12.1 Restrições

| ID | Requisito | Tipo | Critério de aceitação | Verificação | Prior. |
|---|---|---|---|---|---|
| RNF-030 | O sistema deve ser uma aplicação web, acessada por navegador. | Restrição de plataforma | 1. O uso não exige instalar nada além do navegador. 2. Navegadores suportados: Google Chrome, Microsoft Edge, Mozilla Firefox e Apple Safari, na versão estável atual e na anterior, em computador e em celular (DS-07) | D; T (casos de uso principais em cada navegador) | Must |
| RNF-031 | O sistema deve estar em conformidade com a Lei nº 13.709/2018 (LGPD). | Restrição legal | Cada obrigação da LGPD da seção 12.2 tem pelo menos um requisito que a atende, e cada um desses requisitos é verificado pelo seu próprio critério | A (rastreabilidade da seção 12.2) | Must |
| RNF-032 | Se o sistema for operado como serviço (SaaS) pelo fornecedor, os registros de acesso à aplicação devem ser guardados por no mínimo 6 meses, em ambiente controlado e seguro. | Restrição legal (condicional) | Quando operado como serviço: registros de acesso (data, hora e endereço de origem de cada acesso) guardados por pelo menos 6 meses, com as proteções do RNF-004 e do RNF-005 | I | Must |
| RNF-033 | Se os dados forem hospedados ou processados fora do Brasil, a transferência internacional deve se apoiar em um mecanismo do art. 33 da LGPD, como as cláusulas-padrão contratuais aprovadas pela ANPD. | Restrição legal (condicional) | Quando houver hospedagem ou processamento fora do Brasil: existe contrato com mecanismo do art. 33, como as cláusulas-padrão da Resolução CD/ANPD nº 19/2024, e o país de hospedagem consta no aviso de privacidade (RF-053) | I (contratos e aviso) | Must |
| RNF-034 | O fornecedor deve entregar documentação técnica de segurança e de fluxo de dados que permita à organização elaborar o RIPD e responder a fiscalizações. | Restrição legal | A documentação entregue descreve, no mínimo: as categorias de dados tratados, o fluxo dos dados entre os componentes, os locais de armazenamento e as medidas de segurança desta seção 8 | I | Should |
| RNF-035 | Quando existir o aplicativo móvel, ele deve oferecer as mesmas funções em iOS e Android, a partir da mesma API da versão web. | Restrição de plataforma | Para a versão futura: os casos de uso disponíveis na web podem ser concluídos no aplicativo em iOS e em Android, usando só a API do RNF-028 | D (versão futura) | Won't |
| RNF-036 | O futuro aplicativo móvel deve atender à ABNT NBR 17060:2022 (acessibilidade em aplicativos de dispositivos móveis). | Restrição legal; capacidade de interação (inclusividade) | Para a versão futura: o aplicativo atende aos requisitos da ABNT NBR 17060:2022 | A; I (versão futura) | Won't |

**Outras restrições de implementação já definidas na lista geral:**

- A API independente da interface (RNF-028) é a base obrigatória da arquitetura.
- Cada instalação atende a uma única organização (RN-010).
- A interface é em português do Brasil (RNF-016).

### 12.2 Questões legais

| Norma | Obrigação | Requisitos que a atendem |
|---|---|---|
| LGPD, art. 6º (princípios) e art. 46 (segurança) | Medidas técnicas de segurança e privacidade desde a concepção | RNF-001 a RNF-005, RNF-011, RN-013 |
| LGPD, arts. 7º, 8º e 10 (bases legais) | Consentimento não é a base padrão no emprego | RN-012, RF-055 |
| LGPD, arts. 9º e 41 (transparência e encarregado) | Aviso de privacidade com o contato do encarregado | RF-053 |
| LGPD, arts. 18 e 19 (direitos do titular) | Acesso, correção, portabilidade, eliminação, informação sobre compartilhamento | RF-056 a RF-061 |
| LGPD, arts. 15 e 16 (término do tratamento) | Eliminação ao fim do prazo, com as exceções legais | RF-062, RN-011 |
| LGPD, art. 20 (decisões automatizadas) | Indicadores como apoio à decisão humana | RN-008 |
| LGPD, arts. 37 e 38 (registro e RIPD) | Inventário de tratamento e documentação técnica | RF-054, RNF-034 |
| LGPD, art. 48; Resolução CD/ANPD nº 15/2024 (incidentes) | Registro e comunicação de incidentes | RF-063 |
| LGPD, art. 33; Resolução CD/ANPD nº 19/2024 (transferência internacional) | Mecanismo válido para hospedagem fora do país | RNF-033 |
| Marco Civil da Internet, art. 15 | Guarda dos registros de acesso por 6 meses, se operado como serviço | RNF-032 |
| Lei Brasileira de Inclusão, art. 63 | Acessibilidade do sistema web e símbolo de acessibilidade | RNF-017 a RNF-023, RNF-027, RF-065 |
| CF/88, art. 7º, XXX e XXXI; Lei nº 9.029/1995 | Critérios de avaliação sem discriminação | RN-014, RNF-024 |
| Lei nº 14.457/2022, art. 23 | Canal de denúncias separado do sistema de feedback | RN-009, RF-064 |

---

## 13. Interfaces

### 13.1 Interface com o usuário

Interface web responsiva, em português do Brasil, acessível conforme a seção 6.2 e usável nos navegadores da seção 12. As telas serão definidas nos protótipos (#50).

### 13.2 Interfaces de software

| Interface | Direção | Formato | Requisito |
|---|---|---|---|
| API do sistema | Entrada e saída | Documentação publicada em formato padronizado, como a especificação OpenAPI; comunicação protegida pelo RNF-004 | RNF-028 |
| Importação de colaboradores, cargos, equipes e hierarquia | Entrada | CSV no padrão RFC 4180, codificação UTF-8, com cabeçalho na primeira linha | RF-002 |
| Exportação dos dados do titular (portabilidade) | Saída | JSON (RFC 8259) ou CSV (RFC 4180), em UTF-8 | RF-058 |
| Notificações e lembretes | Saída | Notificação dentro do sistema e mensagem de e-mail para o endereço cadastrado (DS-10) | RF-026, RF-037, RF-040 |
| Integração com sistemas de RH e SSO | — | Fora desta versão | RNF-025, RF-004 (Won't) |

O formato do relatório de histórico exportado pelo RH (RF-051) será definido no caso de uso correspondente.

---

## 14. Regras de negócio relacionadas

Larman inclui na especificação suplementar as regras do domínio que afetam a aplicação. Neste projeto, elas já estão na [lista geral](Lista_Geral_Requisitos.md#6-regras-de-negócio), seção 6, e não são repetidas. As que impõem condições de qualidade estão especificadas nesta seção:

| Regra | Onde é especificada aqui |
|---|---|
| RN-003 (feedback não pode ser excluído) | RNF-015 (confirmação antes do envio) |
| RN-004 (modos de identificação do emissor) | Seções 8.1 e 8.3 |
| RN-005 (mínimo de respondentes) | Seção 8.3 |
| RN-008 (indicadores como apoio à decisão) | RNF-007 |
| RN-010 (uma organização por instalação) | Seção 12.1 e RNF-029 |
| RN-011 (prazo de retenção) | RNF-011 (backups), RNF-005 (trilha de auditoria) |

---

## 15. Decisões desta especificação

A lista geral deixou alguns valores para esta especificação. Cada decisão abaixo tem a justificativa e a fonte. A coluna **Situação** indica se a decisão segue uma norma ou as fontes do projeto, ou se ainda depende de validação. As decisões que dependem de validação já estão aplicadas aos critérios desta versão. Se a PO ou a organização decidir de outra forma, a mudança segue a gestão de mudanças do [processo de requisitos](Processo_Requisitos.md) (seção 9).

| # | Questão | Decisão | Justificativa e fonte | Requisitos | Situação |
|---|---|---|---|---|---|
| DS-01 | Qual o volume de usuários para dimensionar o sistema? | Cenário de referência de 500 colaboradores | Limite superior do porte informado nos dois questionários (100 a 499 funcionários). A rede da E02 tem 330 pessoas (E02 §1) | RNF-008, RNF-009 | Fundamentada nas fontes; a validar com as metas do ponto P-10 da lista |
| DS-02 | Como medir o percentil 95 do RNF-008? | Pelo menos 100 medições por operação, no cenário de referência, com o mesmo perfil de rede 4G das ferramentas do navegador | Com 100 medições, os 5% mais lentos somam ao menos 5 medições, o que dá estabilidade ao percentil. O perfil único torna as medições comparáveis | RNF-008 | Decisão de método |
| DS-03 | Quantos usuários simultâneos no pico? | 500, todos os colaboradores do cenário | As fontes não informam como os acessos se distribuem no dia. Testar o pior caso dispensa estimar essa distribuição | RNF-009 | Decisão de método |
| DS-04 | Como demonstrar a escalabilidade? | Teste com o dobro do cenário (1.000), ampliando só a infraestrutura | Mostra o crescimento além do maior porte informado nas fontes sem mudança de código. A meta real depende de cada organização | RNF-029 | Decisão de método |
| DS-05 | Qual o tempo de inatividade e a duração máxima da sessão? | 1 h de inatividade e 24 h de duração total, para todos os perfis | NIST SP 800-63B-4, nível AAL2 (dois fatores): duração total de no máximo 24 h e inatividade de no máximo 1 h. O mesmo limite foi aplicado a todos os perfis porque todos acessam dados pessoais de feedback | RNF-006 | Fundamentada em norma |
| DS-06 | Após quantas tentativas de login sem sucesso o acesso é bloqueado? | Espera crescente após cada falha, de 30 s até 1 h, e desativação do autenticador em 100 falhas consecutivas | NIST SP 800-63B-4, seção 3.2.2: limite de no máximo 100 falhas consecutivas, com técnicas adicionais como a espera crescente ("30 seconds up to an hour"). A espera crescente dificulta ataques de tentativa e erro sem permitir que um atacante bloqueie a conta de outra pessoa com poucas tentativas | RNF-006 | Fundamentada em norma |
| DS-07 | Quais navegadores suportar? | Chrome, Edge, Firefox e Safari, na versão estável atual e na anterior, em computador e celular | Juntos somam cerca de 95% dos acessos no Brasil (StatCounter, setembro de 2026: Chrome 77,1%, Edge 7,7%, Safari 6,6%, Firefox 3,7%). Duas versões cobrem quem ainda não atualizou | RNF-030, RNF-027 | Fundamentada em dados de mercado |
| DS-08 | Com que frequência testar a restauração dos backups? | Antes da abertura de cada ciclo formal | O ciclo formal é o período de maior uso. A PO citou ciclos de 3 ou 4 meses (E01 §5), o que dá ao menos 3 testes por ano | RNF-011 | Fundamentada nas fontes |
| DS-09 | Dados eliminados pela política de retenção continuam nos backups? | Os backups são uma categoria da política de retenção (RF-062). Um dado eliminado deixa de existir nos backups quando termina o prazo de guarda deles | Sem essa regra, a eliminação exigida pela LGPD (art. 16) seria incompleta | RNF-011, RF-062 | A validar com a organização (prazo de guarda dos backups) |
| DS-10 | Por qual canal saem notificações e lembretes? | Dentro do sistema e por e-mail | A PO pede "comunicado de sessão" e "lembrete" sem indicar o canal (E01 §5). A E02 usa WhatsApp (E02 §2), mas integrar com aplicativos de mensagem seria uma integração externa não pedida, critério Won't da lista (C-11) | RF-026, RF-037, RF-040 | A validar com a PO |
| DS-11 | Com que antecedência anunciar uma manutenção? | A antecedência é definida no contrato entre fornecedor e organização. O sistema exibe o aviso antes da janela | O prazo de aviso faz parte do acordo de nível de serviço de cada contrato, e as fontes do projeto não o definem | RNF-010 | Depende do contrato |
| DS-12 | Como registrar quem não respondeu sem quebrar o anonimato? | Separar o controle de participação do conteúdo das respostas, sem dado que ligue os dois | RF-029 exige saber quem não respondeu, e RN-004 exige que ninguém ligue a resposta anônima ao emissor. A separação atende aos dois. A ANPD alerta para o risco de reidentificação na anonimização (pesquisa documental, seção 3.5) | RN-004, RF-029 | Fundamentada nas fontes |
| DS-13 | Como o sistema reconhece termos ofensivos? | Por uma lista de termos mantida pelo administrador | Torna o RNF-024 verificável e deixa a organização ajustar a lista à sua realidade, como pede o RNF-026 | RNF-024 | Decisão de método |

**Metas da lista geral mantidas.** Os valores de 3 s e 2 s (RNF-008), 99,5% (RNF-010), 24 h e 4 h (RNF-011) e de uma única tela (RNF-013) são os da lista geral, que os registrou como decisão provisória no ponto a validar P-10. Esta especificação não altera esses valores, apenas define como medi-los.

---

## 16. Rastreabilidade e cobertura

### 16.1 Requisitos não funcionais

Todos os 36 RNF da lista geral estão especificados neste documento.

| ID | Característica principal | Seção | Verificação | Prior. |
|---|---|---|---|---|
| RNF-001 | Segurança | 8.2 | T | Must |
| RNF-002 | Segurança | 8.2 | T; I | Must |
| RNF-003 | Segurança | 8.2 | I; T | Should |
| RNF-004 | Segurança | 8.2 | A; I | Must |
| RNF-005 | Segurança | 8.2 | T; I | Must |
| RNF-006 | Segurança | 8.2 | T | Should |
| RNF-007 | Adequação funcional | 3 | I; T | Should |
| RNF-008 | Eficiência de desempenho | 4.2 | T | Should |
| RNF-009 | Eficiência de desempenho | 4.2 | T | Should |
| RNF-010 | Confiabilidade | 7 | A; I | Should |
| RNF-011 | Confiabilidade | 7 | T; I | Should |
| RNF-012 | Confiabilidade | 7 | T | Should |
| RNF-013 | Capacidade de interação | 6.1 | I | Should |
| RNF-014 | Capacidade de interação | 6.1 | T | Should |
| RNF-015 | Capacidade de interação | 6.1 | I; T | Should |
| RNF-016 | Capacidade de interação | 6.1 | I | Must |
| RNF-017 | Capacidade de interação | 6.2 | A; I; T | Must |
| RNF-018 | Capacidade de interação | 6.2 | T | Must |
| RNF-019 | Capacidade de interação | 6.2 | A; I | Must |
| RNF-020 | Capacidade de interação | 6.2 | I; T | Must |
| RNF-021 | Capacidade de interação | 6.2 | I; T | Must |
| RNF-022 | Capacidade de interação | 6.2 | T | Must |
| RNF-023 | Capacidade de interação | 6.2 | A; T | Must |
| RNF-024 | Proteção | 11 | T | Could |
| RNF-025 | Compatibilidade | 5 | D | Won't |
| RNF-026 | Manutenibilidade | 9 | D | Should |
| RNF-027 | Flexibilidade | 10 | T | Must |
| RNF-028 | Flexibilidade | 10 | I; A | Must |
| RNF-029 | Flexibilidade | 10 | T | Should |
| RNF-030 | Restrição de plataforma | 12.1 | D; T | Must |
| RNF-031 | Restrição legal | 12.1 | A | Must |
| RNF-032 | Restrição legal | 12.1 | I | Must |
| RNF-033 | Restrição legal | 12.1 | I | Must |
| RNF-034 | Restrição legal | 12.1 | I | Should |
| RNF-035 | Restrição de plataforma | 12.1 | D | Won't |
| RNF-036 | Restrição legal | 12.1 | A; I | Won't |

### 16.2 Checklist da issue #51

| Item | Onde |
|---|---|
| Adequação funcional | Seção 3 |
| Eficiência de desempenho | Seção 4 |
| Compatibilidade | Seção 5 |
| Usabilidade / interação (inclui acessibilidade) | Seção 6 |
| Confiabilidade | Seção 7 |
| Segurança (confidencialidade, anonimato, criptografia, LGPD) | Seção 8: confidencialidade em 8.1 e 8.2; anonimato em 8.3; criptografia no RNF-004; LGPD em 8.4 e 12.2 |
| Manutenibilidade | Seção 9 |
| Portabilidade / flexibilidade (web → mobile) | Seção 10 e RNF-035, RNF-036 |
| Restrições legais e de implementação | Seção 12 |

---

## 17. Referências

**Normas e guias técnicos**

- ISO/IEC. [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) – Systems and software engineering – Systems and software Quality Requirements and Evaluation (SQuaRE) – Product quality model.
- ABNT. [ABNT NBR 17225:2025](https://www2.camara.leg.br/a-camara/estruturaadm/gestao-na-camara-dos-deputados/responsabilidade-social-e-ambiental/acessibilidade/pdfs/ABNTNBR17225AcessibilidadeDigitalparaWeb.pdf) – Acessibilidade em conteúdo e aplicações web – Requisitos.
- ABNT. ABNT NBR 17060:2022 – Acessibilidade em aplicativos de dispositivos móveis – Requisitos.
- W3C. [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/). 2023.
- NIST. [SP 800-63B-4 – Digital Identity Guidelines: Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html). 2025. Seção 2 (níveis AAL, reautenticação) e seção 3.2.2 (limitação de tentativas).
- IETF. [RFC 4180](https://www.rfc-editor.org/rfc/rfc4180) – Common Format and MIME Type for Comma-Separated Values (CSV) Files. 2005.
- IETF. [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259) – The JavaScript Object Notation (JSON) Data Interchange Format. 2017.
- OpenAPI Initiative. [OpenAPI Specification](https://spec.openapis.org/oas/latest.html).

**Legislação**

- BRASIL. [Lei nº 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) – Lei Geral de Proteção de Dados Pessoais (LGPD).
- BRASIL. [Lei nº 12.965/2014](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm) – Marco Civil da Internet.
- BRASIL. [Lei nº 13.146/2015](http://www.planalto.gov.br/ccivil_03/_Ato2015-2018/2015/Lei/L13146.htm) – Lei Brasileira de Inclusão da Pessoa com Deficiência.
- ANPD. Resolução CD/ANPD nº 15/2024 (comunicação de incidentes) e nº 19/2024 (transferência internacional de dados).
- Demais normas trabalhistas citadas: ver a [pesquisa documental](elicitacao/pesquisa-documental/Pesquisa_Documental.md), seção 9.

**Bibliografia e dados**

- LARMAN, C. *Utilizando UML e Padrões: uma introdução à análise e ao projeto orientados a objetos e ao desenvolvimento iterativo*. 3. ed. Porto Alegre: Bookman, 2007. Cap. 7 (Outros requisitos: especificação suplementar e modelo FURPS+).
- STATCOUNTER. [Browser Market Share Brazil](https://gs.statcounter.com/browser-market-share/all/brazil). Consulta em novembro de 2026, dados de setembro de 2026.

**Fontes internas do projeto**

- [Lista Geral de Requisitos](Lista_Geral_Requisitos.md) (#45).
- [Pesquisa documental](elicitacao/pesquisa-documental/Pesquisa_Documental.md) (#33), seções 3, 4 e 6.
- [Entrevista 01](elicitacao/entrevistas/Entrevista01_Adriana.md), §5, §9, §15, §20, §29, §30 e §33. [Entrevista 02](elicitacao/entrevistas/Entrevista02_Eliene.md), §1 e §2.
- [Questionário 01](elicitacao/questionarios/Questionario01_Isabella.md) e [Questionário 02](elicitacao/questionarios/Questionario02_Vaneide.md): porte das empresas e tempo de consolidação.
- [Processo de requisitos](Processo_Requisitos.md) (#31).
