# Pesquisa Documental – LGPD, ISO/IEC 25010 e regulamentações

**Projeto:** Sistema de Gestão de Competências (módulo de Feedback)
**Técnica de elicitação:** Pesquisa documental (leis, regulamentos, normas técnicas)
**Issue:** #33 · **Data de referência da pesquisa:** 12/11/2026
**Artefatos relacionados:** [Requisitos_Pesquisa_Documental.csv](Requisitos_Pesquisa_Documental.csv) (mesma tabela da seção 7, para a matriz de rastreabilidade)

> Este relatório não é parecer jurídico. As interpretações servem para levantar requisitos e devem ser validadas com a Product Owner e, em um projeto real, com o jurídico e o encarregado da organização cliente.

---

## Sumário

1. [Objetivo e método](#1-objetivo-e-método)
2. [Documentos analisados](#2-documentos-analisados)
3. [LGPD – Lei nº 13.709/2018 e regulamentos da ANPD](#3-lgpd--lei-nº-137092018-e-regulamentos-da-anpd)
4. [ISO/IEC 25010:2023 – modelo de qualidade de produto](#4-isoiec-250102023--modelo-de-qualidade-de-produto)
5. [Normas trabalhistas e de RH](#5-normas-trabalhistas-e-de-rh)
6. [Acessibilidade web e responsividade](#6-acessibilidade-web-e-responsividade)
7. [Requisitos extraídos](#7-requisitos-extraídos)
8. [Conflitos e pontos a validar](#8-conflitos-e-pontos-a-validar)
9. [Referências](#9-referências)

---

## 1. Objetivo e método

**Objetivo.** Identificar, nas leis, nos regulamentos e nas normas técnicas aplicáveis, as obrigações e as boas práticas que o sistema de feedback precisa atender, e transformá-las em requisitos rastreáveis até a fonte.

**Método.**

1. Seleção dos documentos a partir do escopo do trabalho (LGPD, ISO/IEC 25010, regulamentações de RH, plataforma web com perspectiva móvel) e dos temas abertos nas fontes já coletadas ([Entrevista 01](../entrevistas/Entrevista01_Adriana.md), [Questionário 01](../questionarios/Questionario01_Isabella.md) e [Questionário 02](../questionarios/Questionario02_Vaneide.md)).
2. Verificação da versão vigente de cada documento em novembro de 2026 (ex.: edição 2023 da ISO/IEC 25010; vigência da nova NR-1 a partir de 26/05/2026).
3. Leitura dos dispositivos pertinentes e registro, para cada um, da implicação para o sistema.
4. Redação de requisitos candidatos, com identificador próprio `RD-xx` (Requisito Documental), seguindo o mesmo padrão dos questionários (`RQ-xx`). Na lista geral (issue #45) eles recebem os identificadores definitivos `RF-`, `RNF-` e `RN-`.

**Classificação usada na seção 7.**

| Campo | Valores |
|---|---|
| Tipo | `RF` funcional · `RNF` não funcional · `RN` regra de negócio · `Restrição` (condição de implantação, contratação ou plataforma) |
| Obrigatoriedade | **Legal** (decorre diretamente de lei ou regulamento) · **Legal (condicional)** (só se aplica em certo cenário) · **Norma técnica** (ABNT, ISO, W3C) · **Boa prática derivada de lei** (meio razoável de cumprir um princípio legal) · **Boa prática** |
| Fonte | Identificador `FD-xx` da tabela da seção 2, com artigo ou critério |

---

## 2. Documentos analisados

| ID | Documento | Tipo | Situação em nov/2026 | Uso no projeto |
|---|---|---|---|---|
| FD-01 | Lei nº 13.709/2018 – Lei Geral de Proteção de Dados Pessoais (LGPD) | Lei federal | Vigente | Base legal, princípios, direitos, segurança, incidentes |
| FD-02 | Resolução CD/ANPD nº 2/2022 – agentes de tratamento de pequeno porte | Regulamento | Vigente | Dispensas e prazos em dobro para pequenas empresas |
| FD-03 | Resolução CD/ANPD nº 15/2024 – comunicação de incidente de segurança | Regulamento | Vigente | Prazos e registro de incidentes |
| FD-04 | Resolução CD/ANPD nº 18/2024 – atuação do encarregado | Regulamento | Vigente | Divulgação do encarregado e suas atribuições |
| FD-05 | Resolução CD/ANPD nº 19/2024 – transferência internacional de dados | Regulamento | Vigente | Hospedagem fora do Brasil |
| FD-06 | ANPD – Guia orientativo de legítimo interesse (fev/2024) | Guia (não vinculante) | Publicado | Base legal no contexto de emprego |
| FD-07 | ANPD – Minuta do Guia de anonimização e pseudonimização (consulta pública de 2024) | Minuta de guia (não vinculante) | Em elaboração | Anonimato e confidencialidade |
| FD-08 | Resolução CD/ANPD nº 31/2025 – Agenda Regulatória 2025-2026 | Regulamento | Vigente | Regulamentação dos direitos do titular ainda pendente |
| FD-09 | Lei nº 12.965/2014 – Marco Civil da Internet | Lei federal | Vigente | Guarda de registros de acesso |
| FD-10 | ISO/IEC 25010:2023 – modelo de qualidade de produto (SQuaRE) | Norma técnica internacional | Vigente (substituiu a edição de 2011) | Estrutura dos requisitos não funcionais |
| FD-11 | Constituição Federal de 1988 – art. 5º, X; art. 7º, XXX e XXXI | Constituição | Vigente | Intimidade e não discriminação |
| FD-12 | Consolidação das Leis do Trabalho (CLT) – arts. 11, 223-B, 223-C e 461 | Lei federal | Vigente | Prescrição, dano extrapatrimonial, equiparação salarial |
| FD-13 | Lei nº 9.029/1995 – práticas discriminatórias na relação de trabalho | Lei federal | Vigente | Critérios proibidos |
| FD-14 | Lei nº 14.611/2023 – igualdade salarial e de critérios remuneratórios (e Decreto nº 11.795/2023) | Lei federal | Vigente | Critérios objetivos de carreira |
| FD-15 | Lei nº 14.457/2022 – Programa Emprega + Mulheres (prevenção ao assédio, art. 23) | Lei federal | Vigente | Canal de denúncias separado |
| FD-16 | NR-1, cap. 1.5 – GRO (redação da Portaria MTE nº 1.419/2024; vigência pela Portaria MTE nº 765/2025) | Norma regulamentadora | Vigente desde 26/05/2026 | Riscos psicossociais |
| FD-17 | Lei nº 13.146/2015 – Lei Brasileira de Inclusão (LBI), art. 63 | Lei federal | Vigente | Obrigação de acessibilidade em sites |
| FD-18 | ABNT NBR 17225:2025 – Acessibilidade em conteúdo e aplicações web | Norma técnica brasileira | Vigente (1ª edição, 11/03/2025) | Requisitos de acessibilidade web |
| FD-19 | W3C – WCAG 2.2 (Diretrizes de Acessibilidade para Conteúdo Web) | Recomendação W3C | Vigente | Critérios de sucesso citados |
| FD-20 | ABNT NBR 17060:2022 – Acessibilidade em aplicativos de dispositivos móveis | Norma técnica brasileira | Vigente | Versão móvel futura |
| FD-21 | eMAG – Modelo de Acessibilidade em Governo Eletrônico | Modelo do governo federal | Vigente (obrigatório só para órgãos públicos) | Referência complementar |

---

## 3. LGPD – Lei nº 13.709/2018 e regulamentos da ANPD

### 3.1 Papéis no tratamento

Em um sistema de feedback vendido a empresas, a **organização cliente** é a **controladora** (decide para que e como os dados de seus colaboradores são tratados) e o **fornecedor do sistema** atua como **operador** (art. 5º, VI e VII). Por isso, vários requisitos da seção 7 aparecem como "dever do controlador; o sistema apoia": o sistema precisa oferecer as ferramentas para que o cliente cumpra a lei (registro das operações, atendimento a titulares, gestão de incidentes).

Os **titulares** são colaboradores, gestores e demais avaliados ou avaliadores. O conteúdo de um feedback é dado pessoal de duas pessoas ao mesmo tempo: de quem recebe (é uma avaliação sobre ele) e de quem emite (é uma opinião atribuível a ele).

### 3.2 Princípios aplicáveis (art. 6º)

| Princípio | O que significa para o sistema | Requisitos |
|---|---|---|
| Finalidade (I) | Os dados servem ao desenvolvimento do colaborador; reutilizá-los para outro fim (ex.: monitorar a saúde) exige nova análise | RD-49 |
| Necessidade (III) | Coletar o mínimo; nada de campos sensíveis "por precaução" | RD-05, RD-06 |
| Livre acesso (IV) e transparência (VI) | O colaborador consulta seus dados; o emissor sabe quem verá sua identidade | RD-01, RD-07, RD-16 |
| Qualidade dos dados (V) | Dados exatos e atualizados; o receptor pode se manifestar sobre um feedback | RD-08, RD-09, RD-43 |
| Segurança (VII) e prevenção (VIII) | Controle de acesso, criptografia, auditoria, backup | RD-14, RD-19 a RD-23, RD-34 |
| Não discriminação (IX) | Critérios e indicadores sem viés discriminatório | RD-45 |
| Responsabilização (X) | Provar o cumprimento: trilha de auditoria, registros e documentação | RD-02, RD-20, RD-30 |

### 3.3 Bases legais (arts. 7º, 8º e 10)

No contexto de emprego, a relação entre empregado e empregador é assimétrica, e o consentimento perde a característica de manifestação **livre** exigida pelo art. 5º, XII. O Guia de legítimo interesse da ANPD (FD-06) destaca justamente essa vulnerabilidade do empregado. Por isso a pesquisa recomenda **não** usar o consentimento como base padrão do sistema (RD-03):

| Operação | Base legal sugerida | Observação |
|---|---|---|
| Cadastro do colaborador, cargo, gestor, competências | Execução de contrato (art. 7º, V) | Necessário à gestão do contrato de trabalho |
| Registro de feedbacks, avaliações, metas e planos de ação | Legítimo interesse (art. 7º, IX, e art. 10) ou execução de contrato | Exige teste de balanceamento documentado e transparência (art. 10, §2º) |
| Retenção do histórico após o desligamento | Exercício regular de direitos em processo (art. 7º, VI) | Limitada ao prazo de prescrição trabalhista (seção 5) |
| Funcionalidades opcionais (ex.: foto de perfil, pesquisa voluntária) | Consentimento (art. 7º, I) | Livre, específico, revogável e sem prejuízo para quem recusar (RD-04) |
| Dados sensíveis (art. 11) | Evitar | Nenhuma funcionalidade do escopo precisa deles (RD-05) |

> O [Termo de Consentimento](../entrevistas/Termo_Consentimento_Entrevista.md) usado nas entrevistas é outro contexto: ali a participação é voluntária e não há vínculo de emprego com o grupo, então o consentimento é adequado.

### 3.4 Direitos do titular (arts. 18 e 19)

| Direito (art. 18) | Funcionalidade correspondente | Requisito |
|---|---|---|
| I e II – confirmação e acesso | Página "Meus dados" com consulta imediata e declaração completa em até 15 dias (art. 19) | RD-07 |
| III – correção | Pedido de correção de dados cadastrais; réplica a um feedback | RD-08, RD-09 |
| IV – anonimização, bloqueio ou eliminação de dados desnecessários | Pedido registrado e acompanhado | RD-11 |
| V – portabilidade | Exportação estruturada (a regulamentação da ANPD sobre direitos do titular ainda está na Agenda Regulatória, FD-08) | RD-10 |
| VI – eliminação dos dados tratados com consentimento | Pedido registrado; ressalvas do art. 16 | RD-11 |
| VII – informação sobre compartilhamento | Lista de terceiros com quem os dados foram compartilhados | RD-12 |
| IX – revogação do consentimento | Revogação simples | RD-04 |
| Atendimento às solicitações (art. 18, §§3º a 5º) | Fila de solicitações para encarregado e RH | RD-13 |

### 3.5 Anonimato, confidencialidade e pseudonimização

Esse é o ponto mais sensível do projeto e aparece em todas as fontes: na entrevista com a PO (§11 e §32), no RQ-04 e RQ-05 (Questionário 01) e no RQ-13 e RQ-14 (Questionário 02, cuja respondente deu nota 1/5 para a chance de ser sincera com o gestor identificado e citou medo de retaliação). A LGPD diferencia:

- **Dado anonimizado** (art. 5º, III, e art. 12): não pode mais ser associado ao titular por meios técnicos razoáveis. **Deixa de ser dado pessoal**, a menos que o processo possa ser revertido.
- **Pseudonimização** (art. 13, §4º): o dado só pode ser associado ao titular com uma informação adicional mantida separadamente pelo controlador. **Continua sendo dado pessoal.**

Na prática, um feedback "anônimo" em que o RH consegue descobrir o emissor **não é anônimo**, e sim **confidencial/pseudonimizado**. Chamá-lo de anônimo violaria a transparência (art. 6º, VI) e quebraria a confiança que a própria PO apontou como risco. A minuta do Guia da ANPD (FD-07) também lembra que a anonimização sempre carrega risco de reidentificação e cita o **k-anonimato** como técnica de medição desse risco. Em um 360º com dois pares, por exemplo, a média já revela quem respondeu o quê.

Derivam daí:

- **RD-15**: três modos de identificação do emissor (identificado, confidencial, anônimo), definidos por tipo de feedback. Isso conversa com a PO, para quem, no feedback formal gestor → colaborador, o emissor é conhecido e o RH tem acesso, enquanto entre pares a identificação "pode ser parametrizada".
- **RD-16**: aviso honesto ao emissor sobre quem verá sua identidade.
- **RD-17**: número mínimo de respondentes antes de exibir agregados. A pesquisa dá base documental ao RQ-14, que o grupo havia proposto no Questionário 02.
- **RD-18**: vínculo emissor–resposta guardado separado do conteúdo e com acesso auditado.

### 3.6 Retenção e eliminação (arts. 15 e 16)

O tratamento termina quando a finalidade é alcançada, e os dados devem ser eliminados, salvo exceções como o cumprimento de obrigação legal ou o uso exclusivo do controlador com os dados anonimizados (art. 16). Para o feedback, entram em jogo três prazos:

| Prazo | Fonte | Efeito no sistema |
|---|---|---|
| Ação trabalhista: até 5 anos durante o contrato, limitada a 2 anos após o desligamento | CLT, art. 11 (FD-12) | Justifica guardar o histórico por até 2 anos após o desligamento, já que ele serve de resguardo jurídico (PO, Entrevista 01 §32) |
| Registros de acesso à aplicação: no mínimo 6 meses | Marco Civil, art. 15 (FD-09) | Logs de acesso guardados se o fornecedor operar como SaaS |
| Registro de incidentes: no mínimo 5 anos | Res. CD/ANPD nº 15/2024, art. 10 (FD-03) | Guarda do registro de incidentes |

O prazo exato é decisão do controlador, e por isso o sistema deve permitir configurá-lo (RD-24).

### 3.7 Encarregado (art. 41 e Resolução CD/ANPD nº 18/2024)

O controlador deve indicar um encarregado e divulgar sua identidade e seus contatos de forma clara (art. 41, §1º). A Resolução nº 18/2024 detalhou a indicação formal, a figura do substituto e as atribuições, entre elas apoiar o registro de incidentes e de operações e a elaboração do RIPD. Agentes de pequeno porte podem ser dispensados de indicar encarregado (Res. nº 2/2022), mas continuam obrigados a manter um canal com o titular. No sistema, isso vira o contato do encarregado no aviso de privacidade (RD-01) e a fila de solicitações (RD-13).

### 3.8 Segurança, incidentes e governança

- **Segurança desde a concepção** (arts. 46 a 49): medidas técnicas e administrativas desde a fase de concepção do produto (art. 46, §2º), e sistemas estruturados para atender aos requisitos de segurança e aos princípios da lei (art. 49). Daí RD-19 a RD-23 e a privacidade por padrão (RD-22).
- **Incidentes** (art. 48 e Res. nº 15/2024): o controlador deve comunicar à ANPD e aos titulares, em até **3 dias úteis** contados do conhecimento, o incidente que possa causar risco ou dano relevante. É possível enviar uma comunicação preliminar e complementá-la em até 20 dias úteis, e agentes de pequeno porte têm prazo em dobro. O sistema precisa detectar e registrar o incidente rápido o suficiente para esse prazo ser viável (RD-26).
- **Decisões automatizadas** (art. 20): o titular pode pedir revisão de decisões tomadas só com base em tratamento automatizado que afetem seus interesses, incluindo perfis profissionais. Os indicadores do sistema são apoio à decisão do gestor, nunca a decisão (RD-27).
- **Registro e RIPD** (arts. 37 e 38): o controlador mantém o registro das operações e pode ter de elaborar o Relatório de Impacto. O sistema ajuda exportando o inventário (RD-02), e o fornecedor entrega a documentação técnica (RD-30).
- **Transferência internacional** (art. 33 e Res. nº 19/2024): hospedar em nuvem fora do país exige um mecanismo válido, como as cláusulas-padrão (RD-28).
- **Sanções** (art. 52): vão de advertência a multa de até 2% do faturamento, limitada a R$ 50 milhões por infração, e incluem ainda publicização da infração, bloqueio ou eliminação dos dados e suspensão do tratamento.

### 3.9 Colaboradores menores de idade (art. 14)

Empresas podem ter aprendizes com menos de 18 anos. O tratamento dos dados de adolescentes deve seguir o seu melhor interesse (art. 14), e daí o RD-29.

---

## 4. ISO/IEC 25010:2023 – modelo de qualidade de produto

### 4.1 O que mudou em relação à edição de 2011

A edição vigente é a de **novembro de 2023**, que substituiu a de 2011. A maior parte do material didático (inclusive a bibliografia da disciplina) ainda descreve o modelo antigo, de 8 características. As mudanças que afetam a especificação suplementar (issue #51) são:

| 2011 | 2023 | Observação |
|---|---|---|
| Usabilidade | **Capacidade de interação** | Ganhou *inclusividade*, *assistência ao usuário* e *autodescritividade*; *estética da interface* virou *engajamento do usuário* |
| Portabilidade | **Flexibilidade** | Ganhou *escalabilidade* |
| — | **Proteção** (*safety*) | Característica nova: evitar danos a pessoas, ao negócio ou ao ambiente |
| Confiabilidade: maturidade | Confiabilidade: **ausência de falhas** (*faultlessness*) | Troca de nome |
| Segurança | Segurança + **resistência** | Subcaracterística nova: resistir a ataques e se recuperar deles |

> As traduções em português são do grupo. Nos documentos, vale indicar o termo em inglês entre parênteses na primeira ocorrência.

### 4.2 Características aplicadas ao sistema

| Característica (2023) | Subcaracterísticas | Por que importa neste sistema | Requisitos |
|---|---|---|---|
| Adequação funcional | completude, correção e adequação funcional | Indicadores e médias corretos e explicáveis; decisões não automatizadas | RD-27, RD-43 |
| Eficiência de desempenho | comportamento temporal, utilização de recursos, capacidade | Picos de acesso no fim dos ciclos de avaliação | RD-31, RD-32 |
| Compatibilidade | coexistência, interoperabilidade | Integração com sistemas de RH e folha; portabilidade de dados | RD-10, RD-39 |
| Capacidade de interação | reconhecimento de adequação, aprendizagem, operabilidade, proteção contra erro do usuário, engajamento, inclusividade, assistência ao usuário, autodescritividade | Usuários que não sabem dar feedback (Questionário 01); acessibilidade; avaliação de par em até 20 min (RQ-11) | RD-06, RD-16, RD-35 a RD-37, RD-50 a RD-58 |
| Confiabilidade | ausência de falhas, disponibilidade, tolerância a falhas, recuperabilidade | Não perder respostas (a PO relatou um sistema análogo que descartava o cadastro incompleto, Entrevista 01 §33) | RD-33 a RD-35 |
| Segurança | confidencialidade, integridade, não repúdio, responsabilização, autenticidade, resistência | Núcleo da LGPD e do anonimato | RD-14, RD-17 a RD-23, RD-47 |
| Manutenibilidade | modularidade, reusabilidade, analisabilidade, modificabilidade, testabilidade | Competências e questionários mudam por cargo e por organização (Entrevista 01 §15) | RD-40, RD-41 |
| Flexibilidade | adaptabilidade, escalabilidade, instalabilidade, substituibilidade | Web hoje e móvel no futuro (escopo do trabalho) | RD-41, RD-42, RD-56 |
| Proteção (*safety*) | restrição operacional, identificação de risco, falha segura, alerta de perigo, integração segura | Feedback mal escrito causa dano psicológico e jurídico (a PO reforçou que a ferramenta é de desenvolvimento, não punitiva, Entrevista 01 §32) | RD-38 |

As metas numéricas (tempo de resposta, disponibilidade, RPO/RTO) são **propostas** para dar verificabilidade aos RNF e devem ser validadas antes da especificação suplementar.

---

## 5. Normas trabalhistas e de RH

| Norma | Ponto relevante | Implicação para o sistema | Requisitos |
|---|---|---|---|
| CF/88, art. 5º, X | Inviolabilidade da intimidade, da vida privada, da honra e da imagem | Feedback trata de comportamento no trabalho, não de personalidade ou vida pessoal, como disse a PO: o feedback é "sempre baseada em fatos" (Entrevista 01 §11) | RD-44 |
| CLT, arts. 223-B e 223-C | Dano extrapatrimonial ao trabalhador (honra, imagem, intimidade, autoestima etc.) | Registro escrito de feedback ofensivo é prova contra o empregador; alertas de linguagem | RD-38, RD-44 |
| CF/88, art. 7º, XXX e XXXI; Lei nº 9.029/1995, art. 1º | Proibição de prática discriminatória para acesso ao emprego ou sua manutenção (sexo, origem, raça, cor, estado civil, situação familiar, deficiência, idade, entre outros) | Questionários e competências sem critérios discriminatórios | RD-45 |
| CLT, art. 461; Lei nº 14.611/2023 | Igualdade salarial e de critérios remuneratórios; empresas com 100 ou mais empregados publicam relatório semestral de transparência com dados anonimizados | A PO definiu que o foco é desenvolvimento, não promoção ou salário (Entrevista 01 §8). Se o cliente usar os resultados para carreira, os critérios precisam ser objetivos e iguais para todos | RD-46 |
| CLT, art. 11 | Prescrição: 5 anos durante o contrato, até 2 anos após o desligamento | Prazo de retenção do histórico, que serve de resguardo jurídico em desligamentos (Entrevista 01 §32) | RD-24, RD-47 |
| Lei nº 14.457/2022, art. 23 | Empresas obrigadas a ter CIPA devem manter procedimentos para receber e acompanhar denúncias de assédio, com anonimato do denunciante | Confirma a PO ("denúncia é denúncia"): o sistema de feedback não substitui o canal de denúncias, mas aponta para ele | RD-48 |
| NR-1, cap. 1.5 (Portaria MTE nº 1.419/2024) | Desde 26/05/2026, o Gerenciamento de Riscos Ocupacionais deve incluir os fatores de risco psicossociais (em vigor após o adiamento feito pela Portaria MTE nº 765/2025) | Liderança sem suporte, comunicação deficiente e assédio moral são fatores psicossociais, e um processo de feedback bem conduzido ajuda a mitigá-los. Dados individuais de feedback, porém, não podem virar monitoramento de saúde | RD-38, RD-49 |

> Convenções e acordos coletivos podem trazer regras próprias sobre avaliação de desempenho, a verificar caso a caso em cada cliente.

---

## 6. Acessibilidade web e responsividade

### 6.1 Obrigação legal

O **art. 63 da LBI** (FD-17) torna obrigatória a acessibilidade nos sites mantidos por empresas com sede ou representação comercial no país, conforme as melhores práticas internacionais, e o §1º exige símbolo de acessibilidade em destaque. Como o sistema é usado por colaboradores das empresas clientes, inclusive pessoas com deficiência, a obrigação também se apoia no art. 34 da LBI, que garante à pessoa com deficiência ambiente de trabalho acessível e inclusivo, em igualdade de oportunidades.

### 6.2 Normas técnicas

- **ABNT NBR 17225:2025** (FD-18): primeira norma brasileira de acessibilidade em conteúdo e aplicações web, publicada em 11/03/2025 e baseada nas WCAG 2.2. Tem 146 diretrizes divididas em **requisitos** (o mínimo) e **recomendações** (ir além), e pode ser consultada gratuitamente. Ela é a referência técnica mais direta para cumprir o art. 63.
- **WCAG 2.2** (FD-19): adotamos os critérios de **nível A e AA** como meta, que é o patamar mais usado como referência de conformidade. A NBR 17225 parte dessas mesmas diretrizes, então os critérios citados abaixo servem de checklist para as duas.
- **ABNT NBR 17060:2022** (FD-20): acessibilidade em aplicativos móveis. Vale para a versão móvel futura (RD-59).
- **eMAG** (FD-21): obrigatório apenas para órgãos públicos federais; serve como referência complementar.

### 6.3 Critérios mais relevantes para este sistema

O sistema é composto basicamente de **formulários** (feedback, questionários, metas), **painéis com gráficos** (evolução) e **uso em telas pequenas** (perspectiva móvel). Os critérios WCAG 2.2 que mais pesam nesses casos:

| Situação | Critérios WCAG 2.2 | Requisito |
|---|---|---|
| Responder questionários e escrever feedback | 3.3.1 identificação de erro · 3.3.2 rótulos ou instruções · 3.3.3 sugestão de erro · 3.3.7 entrada redundante (novo na 2.2) | RD-54 |
| Login | 3.3.8 autenticação acessível, mínimo (novo na 2.2) | RD-55 |
| Gráficos de evolução e status de metas | 1.1.1 conteúdo não textual · 1.4.1 uso de cor · 1.4.11 contraste não textual | RD-52, RD-53 |
| Navegação | 2.1.1 teclado · 2.4.7 foco visível · 2.4.11 foco não encoberto (novo na 2.2) | RD-51 |
| Celular | 1.3.4 orientação · 1.4.10 refluxo a 320 px · 2.5.8 tamanho do alvo, mínimo de 24 × 24 px (novo na 2.2) | RD-56 |
| Leitores de tela e ampliação | 1.3.1 informações e relações · 1.4.4 redimensionar texto · 3.1.1 idioma da página · 4.1.2 nome, função, valor | RD-57 |

### 6.4 Perspectiva móvel

Os questionários divergem: no Questionário 01, "responder pelo celular" foi avaliado como "nada útil"; no Questionário 02, como "muito útil" (RQ-20). Independentemente disso, o enunciado do trabalho exige perspectiva de uso em dispositivos móveis. A pesquisa conclui que a **interface responsiva** (RD-56) e a **API separada da interface** (RD-41) são necessárias desde a primeira versão, e que o **aplicativo nativo** pode ficar para depois (RD-59).

---

## 7. Requisitos extraídos

Total de **59 requisitos candidatos**. Os mesmos dados estão em [Requisitos_Pesquisa_Documental.csv](Requisitos_Pesquisa_Documental.csv).

**Por tipo:** RF: 16 · RNF: 28 · RN: 11 · Restrição: 4  
**Por obrigatoriedade:** Legal: 27 · Norma técnica: 20 · Boa prática derivada de lei: 8 · Boa prática: 3 · Legal + norma técnica: 1

| ID | Requisito | Tipo | Característica ISO/IEC 25010:2023 | Fonte(s) | Obrigatoriedade | Relação com outras fontes |
|---|---|---|---|---|---|---|
| RD-01 | O sistema deve disponibilizar, em local fixo e acessível de qualquer tela, o aviso de privacidade com finalidades, bases legais, compartilhamentos, prazos de retenção, direitos do titular e identidade e contato do encarregado. | RF | — | FD-01 (arts. 6º VI, 9º, 41 §1º); FD-04 | Legal | — |
| RD-02 | O sistema deve permitir que o administrador da organização (controlador) cadastre a finalidade e a base legal de cada categoria de dado tratado e exporte esse inventário, para apoiar o registro das operações e o RIPD. | RF | — | FD-01 (arts. 37, 38) | Legal (dever do controlador; o sistema apoia) | — |
| RD-03 | O consentimento não deve ser a base legal padrão para tratar dados de feedback de empregados. O tratamento principal se apoia em execução de contrato ou legítimo interesse; o consentimento fica restrito a funcionalidades opcionais, e recusá-lo não pode bloquear o uso do sistema nem gerar prejuízo ao colaborador. | RN | — | FD-01 (arts. 7º, 8º, 10); FD-06 | Legal | Ajusta RQ-12 (ver seção 8) |
| RD-04 | Quando houver tratamento baseado em consentimento, o sistema deve registrar quem consentiu, quando, para qual finalidade e em qual versão do termo, e permitir a revogação a qualquer momento por meio tão simples quanto o usado para consentir. | RF | — | FD-01 (art. 8º §§2º e 5º) | Legal | RQ-12 |
| RD-05 | Cadastros e formulários devem coletar apenas os dados necessários à finalidade de feedback e desenvolvimento. É vedado criar campos para dados pessoais sensíveis (saúde, origem racial ou étnica, religião, opinião política, filiação sindical, vida sexual, dado genético ou biométrico). | RN | — | FD-01 (arts. 5º II, 6º III, 11) | Legal | — |
| RD-06 | Nos campos de texto livre, o sistema deve orientar o emissor a descrever fatos e comportamentos observáveis e a não incluir dados sensíveis, informações de saúde ou dados de terceiros. | RF | Capacidade de interação (assistência ao usuário) | FD-01 (arts. 6º III, 11); FD-12 (art. 223-C) | Boa prática derivada de lei | Entrevista 01 §11 e §3 |
| RD-07 | O colaborador deve poder confirmar a existência de tratamento e acessar seus dados pessoais pelo próprio sistema: de forma simplificada e imediata, ou por declaração completa (origem, critérios, finalidade) em até 15 dias. | RF | — | FD-01 (arts. 18 I-II, 19) | Legal | — |
| RD-08 | O colaborador deve poder solicitar a correção de dados cadastrais incompletos, inexatos ou desatualizados. | RF | — | FD-01 (art. 18 III) | Legal | — |
| RD-09 | O receptor deve poder registrar uma manifestação (réplica) sobre um feedback recebido, sem alterar o conteúdo original escrito pelo emissor. | RF | — | FD-01 (arts. 6º V, 18 III) | Boa prática derivada de lei | — |
| RD-10 | O colaborador deve poder exportar seus dados (cadastro, feedbacks recebidos, metas e planos de ação) em formato estruturado e legível por máquina (ex.: JSON ou CSV). | RF | Compatibilidade (interoperabilidade) | FD-01 (arts. 18 V, 19 §3º); FD-08 | Legal | — |
| RD-11 | O colaborador deve poder solicitar anonimização, bloqueio ou eliminação de dados desnecessários ou excessivos, e a eliminação dos dados tratados com base em consentimento, ressalvadas as hipóteses de conservação do art. 16. | RF | — | FD-01 (arts. 16, 18 IV e VI) | Legal | — |
| RD-12 | O sistema deve informar ao colaborador com quais entidades públicas e privadas seus dados foram compartilhados (ex.: consultoria externa de RH, fornecedor de hospedagem). | RF | — | FD-01 (art. 18 VII) | Legal | — |
| RD-13 | O sistema deve oferecer ao encarregado e ao RH uma fila de solicitações de titulares, com data de abertura, prazo, status, responsável, histórico e resposta enviada. | RF | — | FD-01 (arts. 18 §§3º-5º, 19, 41 §2º); FD-04 | Legal (dever do controlador; o sistema apoia) | — |
| RD-14 | O acesso a feedbacks e resultados deve ser controlado por perfil e por vínculo hierárquico: o resultado de um colaborador só é visível para ele próprio, seu gestor direto e o RH. | RNF | Segurança (confidencialidade) | FD-01 (arts. 6º VII, 46); FD-10 | Legal | RQ-05; Entrevista 01 §11; Questionário 02 §9 (Diretoria) |
| RD-15 | Cada tipo de feedback deve ter um modo de identificação do emissor definido pelo administrador: identificado (padrão para gestor → colaborador), confidencial (identidade oculta para o receptor e visível apenas ao RH) ou anônimo (nenhum perfil consegue vincular a resposta ao emissor). | RN | — | FD-01 (arts. 5º III e XI, 12, 13 §4º); FD-07 | Boa prática derivada de lei | RQ-04, RQ-13; Entrevista 01 §11 |
| RD-16 | Antes do envio, o sistema deve informar ao emissor, em linguagem clara, quem poderá ver sua identidade e seu texto. O rótulo "anônimo" só pode ser usado quando nenhum perfil, inclusive RH e administrador, conseguir reidentificar o emissor. | RF | Capacidade de interação (autodescritividade) | FD-01 (arts. 6º VI, 9º); FD-07 | Legal | Entrevista 01 §32 |
| RD-17 | Resultados agregados de fontes confidenciais ou anônimas (pares, 360º, avaliação ascendente) só podem ser exibidos quando houver um número mínimo de respondentes (sugestão: 3, configurável). Abaixo desse mínimo, as respostas são agrupadas em outra categoria ou omitidas. | RN | Segurança (confidencialidade) | FD-07 (Apêndice III, k-anonimato); FD-01 (art. 12) | Boa prática | RQ-14 |
| RD-18 | Em feedbacks confidenciais, o vínculo entre emissor e resposta deve ser armazenado separado do conteúdo (pseudonimização), com acesso restrito ao RH e registrado em trilha de auditoria. | RNF | Segurança (confidencialidade, responsabilização) | FD-01 (arts. 13 §4º, 46); FD-07 | Boa prática derivada de lei | — |
| RD-19 | Dados pessoais e conteúdo de feedback devem ser criptografados em trânsito (TLS 1.2 ou superior) e em repouso. | RNF | Segurança (confidencialidade, integridade) | FD-01 (art. 46); FD-10 | Legal (medida técnica de segurança) | — |
| RD-20 | O sistema deve manter trilha de auditoria inalterável dos acessos e alterações a dados pessoais e feedbacks (quem, quando, o quê, de onde), incluindo toda consulta à identidade de emissores confidenciais. | RNF | Segurança (responsabilização, não repúdio) | FD-01 (arts. 6º X, 37, 46); FD-10 | Legal | — |
| RD-21 | O sistema deve exigir autenticação forte: autenticação em dois fatores para RH e administradores, bloqueio após tentativas sucessivas de login e expiração de sessão por inatividade. | RNF | Segurança (autenticidade, resistência) | FD-01 (art. 46); FD-10 | Boa prática derivada de lei | — |
| RD-22 | As configurações padrão devem ser as mais protetivas (privacidade por padrão): feedbacks novos nascem visíveis apenas ao público mínimo, e qualquer ampliação de visibilidade exige ação explícita. | RNF | Segurança (confidencialidade) | FD-01 (arts. 46 §2º, 49) | Legal | — |
| RD-23 | Os dados de cada organização cliente devem ficar logicamente isolados dos dados das demais. | RNF | Segurança (confidencialidade) | FD-01 (art. 46); FD-10 | Boa prática | — |
| RD-24 | O sistema deve ter política de retenção configurável por categoria (feedbacks, planos de ação, logs), com eliminação ou anonimização automática ao fim do prazo, inclusive após o desligamento, e com bloqueio da eliminação quando houver processo judicial em curso. Sugestão de padrão: manter durante o contrato e por até 2 anos após o desligamento. | RF | — | FD-01 (arts. 7º VI, 15, 16); FD-12 (art. 11) | Legal | Entrevista 01 §32 |
| RD-25 | Se o fornecedor operar o sistema como serviço (SaaS), os registros de acesso à aplicação devem ser guardados por no mínimo 6 meses, em ambiente controlado e seguro. | Restrição | Segurança (responsabilização) | FD-09 (art. 15) | Legal (condicional) | — |
| RD-26 | O sistema deve apoiar a gestão de incidentes: alertas de eventos suspeitos, registro do incidente (data, dados e titulares afetados, medidas adotadas), geração da lista de titulares a comunicar e guarda do registro por no mínimo 5 anos, para que o controlador consiga comunicar a ANPD e os titulares em até 3 dias úteis. | RF | Segurança (resistência) | FD-01 (art. 48); FD-03 (arts. 6º, 9º, 10) | Legal (dever do controlador; o sistema apoia) | — |
| RD-27 | Indicadores, pontuações e gráficos são apoio à decisão humana. O sistema não toma automaticamente decisões sobre o colaborador (desligamento, promoção, remuneração) e, quando calcular uma pontuação, deve exibir os critérios e os dados usados no cálculo. | RN | Adequação funcional (correção) | FD-01 (art. 20) | Legal | — |
| RD-28 | Se os dados forem hospedados ou processados fora do Brasil, a transferência internacional deve se apoiar em um mecanismo do art. 33 da LGPD, como as cláusulas-padrão contratuais aprovadas pela ANPD. | Restrição | — | FD-01 (art. 33); FD-05 | Legal (condicional) | — |
| RD-29 | O sistema deve permitir identificar colaboradores menores de 18 anos (ex.: aprendizes), para que seus dados sejam tratados no seu melhor interesse e compartilhados apenas no estritamente necessário. | RN | — | FD-01 (art. 14) | Legal | — |
| RD-30 | O fornecedor deve entregar documentação técnica de segurança e de fluxo de dados que permita ao controlador elaborar o RIPD e responder a fiscalizações. | Restrição | — | FD-01 (arts. 38, 39, 50) | Legal (dever do controlador; o fornecedor apoia) | — |
| RD-31 | As telas principais (painel, formulário de feedback, histórico) devem carregar em até 3 s e o envio de um feedback deve ser confirmado em até 2 s, no percentil 95, em conexão 4G. (Metas propostas, a validar.) | RNF | Eficiência de desempenho (comportamento temporal) | FD-10 | Norma técnica (meta a validar) | — |
| RD-32 | O sistema deve suportar o pico de um ciclo formal de avaliação, quando a maior parte dos colaboradores responde na mesma semana, sem degradar as metas de RD-31. (Volume a definir com o cliente.) | RNF | Eficiência de desempenho (capacidade) | FD-10 | Norma técnica (meta a validar) | — |
| RD-33 | Disponibilidade mínima de 99,5% ao mês, com janelas de manutenção comunicadas e fora dos prazos de ciclos de avaliação. | RNF | Confiabilidade (disponibilidade) | FD-10; FD-01 (art. 46) | Norma técnica (meta a validar) | — |
| RD-34 | Backups criptografados diários, com perda máxima de 24 h de dados (RPO) e restauração em até 4 h (RTO), e testes periódicos de restauração. | RNF | Confiabilidade (recuperabilidade) | FD-10; FD-01 (art. 46) | Norma técnica (meta a validar) | — |
| RD-35 | Respostas a feedbacks e questionários devem ser salvas automaticamente como rascunho, para que nada se perca em caso de queda de conexão, sessão expirada ou campos obrigatórios ainda em branco. | RNF | Confiabilidade (tolerância a falhas); Capacidade de interação (proteção contra erro do usuário) | FD-10 | Norma técnica | Entrevista 01 §33 |
| RD-36 | Formulários devem validar os campos com mensagens claras e pedir confirmação antes de ações irreversíveis (enviar feedback, encerrar ciclo, excluir meta). | RNF | Capacidade de interação (proteção contra erro do usuário) | FD-10; FD-19 (3.3.1, 3.3.3, 3.3.4) | Norma técnica | — |
| RD-37 | O sistema deve oferecer ajuda contextual para quem escreve feedback (exemplos, modelos de feedback positivo e construtivo, dicas de linguagem). | RNF | Capacidade de interação (assistência ao usuário, aprendizagem) | FD-10 | Norma técnica | RQ-03 |
| RD-38 | Antes do envio, o sistema deve sinalizar ao emissor termos potencialmente ofensivos ou discriminatórios, sugerindo revisão (alerta, não bloqueio). | RNF | Proteção (alerta de perigo) | FD-10; FD-12 (art. 223-C); FD-13; FD-16 | Boa prática | Entrevista 01 §32 |
| RD-39 | O sistema deve permitir importar e exportar colaboradores, cargos, competências e estrutura organizacional (CSV e API documentada), para integração com sistemas de RH e folha. | RNF | Compatibilidade (interoperabilidade) | FD-10 | Norma técnica | — |
| RD-40 | Competências, questionários, modalidades de feedback e ciclos devem ser parametrizáveis pelo administrador, sem alteração de código. | RNF | Manutenibilidade (modificabilidade); Flexibilidade (adaptabilidade) | FD-10 | Norma técnica | Entrevista 01 §15; RQ-01, RQ-02 |
| RD-41 | O back-end deve expor todas as funcionalidades por uma API independente da interface web, de modo que o futuro aplicativo móvel reutilize as mesmas regras de negócio. | RNF | Flexibilidade (adaptabilidade); Manutenibilidade (modularidade, reusabilidade) | FD-10 | Norma técnica | Escopo (README) |
| RD-42 | A arquitetura deve permitir aumentar o número de organizações e de colaboradores sem reescrever o sistema (escala horizontal). | RNF | Flexibilidade (escalabilidade) | FD-10 | Norma técnica | — |
| RD-43 | Toda média, tendência ou gráfico exibido deve informar o período e o número de respostas que o compõem. | RNF | Adequação funcional (correção); Capacidade de interação (autodescritividade) | FD-10; FD-01 (art. 6º V) | Norma técnica | — |
| RD-44 | Cada feedback deve registrar fatos e comportamentos observáveis, com data e contexto. Questionários não podem pedir avaliação de traços de personalidade ou de aspectos da vida privada. | RN | — | FD-11 (art. 5º X); FD-12 (arts. 223-B, 223-C) | Boa prática derivada de lei | Entrevista 01 §3 e §11 |
| RD-45 | Competências e perguntas não podem usar critérios discriminatórios, como sexo, origem, raça, cor, estado civil, situação familiar, deficiência ou idade. | RN | — | FD-11 (art. 7º XXX e XXXI); FD-13 (art. 1º); FD-14 | Legal | — |
| RD-46 | O sistema não calcula salário, promoção nem desligamento. Se a organização usar os resultados como insumo de carreira, os critérios devem estar documentados e ser os mesmos para todos no mesmo cargo. | RN | — | FD-12 (art. 461); FD-14 | Legal (condicional) | Entrevista 01 §8 |
| RD-47 | Feedbacks e planos de ação formam um histórico datado e íntegro: edições geram nova versão sem apagar a anterior, e o RH pode exportar o histórico de um colaborador em relatório. | RF | Segurança (integridade) | FD-12 (art. 11); FD-01 (art. 6º V) | Boa prática derivada de lei | Entrevista 01 §32; RQ-09 |
| RD-48 | O sistema não é canal de denúncia. Deve manter um atalho visível para o canal de denúncias da organização e orientar o usuário a usá-lo quando o relato for de assédio ou de conduta grave. | RN | — | FD-15 (art. 23) | Legal (a organização deve ter o canal) | Entrevista 01 §32 |
| RD-49 | Dados individuais de feedback não podem ser reutilizados para monitorar a saúde do colaborador. Se a organização quiser usá-los na gestão de riscos psicossociais (GRO/PGR), só poderá fazê-lo com indicadores agregados e anonimizados. | RN | — | FD-16; FD-01 (arts. 6º I, 11) | Boa prática derivada de lei | — |
| RD-50 | A interface web deve atender aos requisitos da ABNT NBR 17225:2025 e aos critérios de nível A e AA das WCAG 2.2. | RNF | Capacidade de interação (inclusividade) | FD-17 (art. 63); FD-18; FD-19 | Legal + norma técnica | — |
| RD-51 | Todas as funcionalidades devem ser operáveis por teclado, com foco sempre visível e não encoberto por outros elementos. | RNF | Capacidade de interação (inclusividade, operabilidade) | FD-18; FD-19 (2.1.1, 2.4.7, 2.4.11) | Norma técnica | — |
| RD-52 | O contraste deve ser de no mínimo 4,5:1 para texto normal e 3:1 para texto grande e componentes de interface. A cor não pode ser o único meio de transmitir informação (ex.: status de metas, linhas de gráficos). | RNF | Capacidade de interação (inclusividade) | FD-18; FD-19 (1.4.1, 1.4.3, 1.4.11) | Norma técnica | — |
| RD-53 | Gráficos de evolução e indicadores devem ter alternativa textual equivalente (resumo e tabela de dados). | RNF | Capacidade de interação (inclusividade) | FD-18; FD-19 (1.1.1) | Norma técnica | Escopo: análise robusta |
| RD-54 | Formulários devem ter rótulos e instruções, identificar o erro e sugerir a correção, e não pedir de novo informação já fornecida no mesmo processo. | RNF | Capacidade de interação (inclusividade, proteção contra erro do usuário) | FD-18; FD-19 (3.3.1, 3.3.2, 3.3.3, 3.3.7) | Norma técnica | — |
| RD-55 | O login não pode depender de teste cognitivo sem alternativa: deve permitir colar a senha e usar gerenciadores de senha. | RNF | Capacidade de interação (inclusividade); Segurança (autenticidade) | FD-19 (3.3.8) | Norma técnica | — |
| RD-56 | A interface deve ser responsiva: sem rolagem horizontal a 320 px de largura, funcional em retrato e paisagem, com alvos de toque de no mínimo 24 × 24 px CSS. | RNF | Flexibilidade (adaptabilidade); Capacidade de interação (operabilidade) | FD-19 (1.3.4, 1.4.10, 2.5.8); FD-18 | Norma técnica | RQ-20; Escopo (README) |
| RD-57 | As páginas devem usar HTML semântico (títulos, regiões, rótulos), declarar o idioma pt-BR, aceitar texto ampliado em 200% sem perda de conteúdo e funcionar com leitores de tela. | RNF | Capacidade de interação (inclusividade) | FD-18; FD-19 (1.3.1, 1.4.4, 3.1.1, 4.1.2) | Norma técnica | — |
| RD-58 | O sistema deve exibir o símbolo de acessibilidade em destaque e uma página de declaração de acessibilidade com o nível de conformidade e um canal para reportar barreiras. | RF | Capacidade de interação (inclusividade) | FD-17 (art. 63 §1º) | Legal | — |
| RD-59 | O futuro aplicativo móvel deve atender à ABNT NBR 17060:2022 (acessibilidade em aplicativos de dispositivos móveis). | Restrição | Capacidade de interação (inclusividade) | FD-20; FD-17 (art. 63) | Norma técnica | Escopo (README) |

---

## 8. Conflitos e pontos a validar

| # | Ponto | Fontes em tensão | Proposta | Validar com |
|---|---|---|---|---|
| 1 | **RQ-12 x RD-03.** O Questionário 01 derivou "registrar consentimento antes da coleta". No sistema, porém, o consentimento não deve ser a base padrão no contexto de emprego | RQ-12; LGPD arts. 7º e 8º; FD-06 | Manter RQ-12 apenas para funcionalidades opcionais (RD-04) e usar RD-03 como regra geral | PO / grupo (issue #45) |
| 2 | **Quem vê a identidade do emissor.** A PO disse que o RH pode ver quem deu o feedback e que, no feedback formal, o receptor sabe quem é o emissor. Já o RQ-13 pede que nenhum perfil veja o autor de uma avaliação anônima, e as respondentes deram nota 1/5 e 2/5 para a sinceridade com o gestor identificado | Entrevista 01 §11 e §32; RQ-04; RQ-13; LGPD art. 6º VI | Três modos por tipo de feedback (RD-15) e rótulo honesto (RD-16). Se o RH puder ver, o modo se chama "confidencial", não "anônimo" | PO |
| 3 | **Direito de acesso x identidade do emissor confidencial.** Ao pedir acesso aos seus dados (art. 18), o avaliado poderia querer saber quem o avaliou | LGPD art. 18 II; RD-15 | Entregar o conteúdo sem a identidade de emissores confidenciais, com a justificativa registrada no RIPD (os direitos de um titular não anulam os de outro) | PO; em projeto real, jurídico |
| 4 | **Prazo padrão de retenção** | CLT art. 11; LGPD art. 16 | Padrão sugerido: duração do contrato + 2 anos, configurável (RD-24) | PO |
| 5 | **Número mínimo de respondentes** para exibir agregados | FD-07; RQ-14 | Sugestão: 3, configurável (RD-17) | PO |
| 6 | **Uso dos resultados para promoção ou salário** | Entrevista 01 §8; CLT art. 461; Lei nº 14.611/2023 | Fora do escopo; RD-46 limita o sistema a apoiar, sem calcular | PO |
| 7 | **Metas numéricas dos RNF** (desempenho, disponibilidade, RPO/RTO) | ISO/IEC 25010 | Valores propostos em RD-31 a RD-34 | Grupo (issue #51) |
| 8 | **Regulamentação pendente.** A ANPD ainda não publicou o regulamento de direitos do titular (portabilidade, prazos e formatos), que está na Agenda Regulatória | FD-08 | Projetar RD-07 a RD-13 de forma configurável e revisar quando o regulamento sair | Grupo |
| 9 | **Diretoria vendo resultados individuais.** O Questionário 02 incluiu a Diretoria entre quem vê o resultado; o Questionário 01 e a PO citam só avaliado, gestor direto e RH | RQ-05; Questionário 02 §9; LGPD art. 6º III | Diretoria vê apenas indicadores agregados, respeitando o mínimo de respondentes (RD-14, RD-17) | PO |

---

## 9. Referências

**Legislação e regulamentos**

- BRASIL. [Lei nº 13.709, de 14 de agosto de 2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) – Lei Geral de Proteção de Dados Pessoais (LGPD).
- ANPD. [Resolução CD/ANPD nº 2, de 27 de janeiro de 2022](https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022) – Regulamento de aplicação da LGPD para agentes de tratamento de pequeno porte.
- ANPD. [Resolução CD/ANPD nº 15, de 24 de abril de 2024](https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-15-de-24-de-abril-de-2024-556243024) – Regulamento de Comunicação de Incidente de Segurança.
- ANPD. [Resolução CD/ANPD nº 18, de 16 de julho de 2024](https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-18-de-16-de-julho-de-2024-572632074) – Regulamento sobre a atuação do encarregado.
- ANPD. Resolução CD/ANPD nº 19, de 23 de agosto de 2024 – Regulamento de Transferência Internacional de Dados.
- ANPD. Guia Orientativo – Hipóteses legais de tratamento de dados pessoais: legítimo interesse. Fev. 2024.
- ANPD. [Minuta do Guia de Anonimização e Pseudonimização para a Proteção de Dados Pessoais – Nota Técnica de abertura da consulta](https://www.gov.br/anpd/pt-br/acesso-a-informacao/participacao-social/outras-acoes/ts-01-2024-nota-tenica-6-de-abertura.pdf/@@display-file/file). 2024.
- ANPD. Resolução CD/ANPD nº 31, de 22 de dezembro de 2025 – altera a Agenda Regulatória 2025-2026 ([resumo](https://legismap.com.br/conteudos/artigos-e-noticias/anpd-publica-mapa-de-temas-prioritarios-para-o-bienio-2026-2027-e-atualiza-agenda-regulatoria-2025-2026)).
- BRASIL. [Lei nº 12.965, de 23 de abril de 2014](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm) – Marco Civil da Internet.
- BRASIL. [Constituição da República Federativa do Brasil de 1988](https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm).
- BRASIL. [Decreto-Lei nº 5.452, de 1º de maio de 1943](https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452.htm) – Consolidação das Leis do Trabalho (CLT).
- BRASIL. [Lei nº 9.029, de 13 de abril de 1995](https://www.planalto.gov.br/ccivil_03/leis/l9029.htm) – Proíbe práticas discriminatórias na relação de trabalho.
- BRASIL. [Lei nº 14.611, de 3 de julho de 2023](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14611.htm) – Igualdade salarial e de critérios remuneratórios entre mulheres e homens.
- BRASIL. [Lei nº 14.457, de 21 de setembro de 2022](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14457.htm) – Programa Emprega + Mulheres.
- MTE. Portaria MTE nº 1.419, de 27 de agosto de 2024 – nova redação do capítulo 1.5 da NR-1; Portaria MTE nº 765, de 15 de maio de 2025 – prorroga a vigência para maio de 2026.
- BRASIL. [Lei nº 13.146, de 6 de julho de 2015](http://www.planalto.gov.br/ccivil_03/_Ato2015-2018/2015/Lei/L13146.htm) – Lei Brasileira de Inclusão da Pessoa com Deficiência.

**Normas técnicas**

- ISO/IEC. [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) – Systems and software engineering – SQuaRE – Product quality model. Resumo das mudanças: [arc42 – ISO 25010 update 2023](https://quality.arc42.org/articles/iso-25010-update-2023).
- ABNT. [ABNT NBR 17225:2025](https://www2.camara.leg.br/a-camara/estruturaadm/gestao-na-camara-dos-deputados/responsabilidade-social-e-ambiental/acessibilidade/pdfs/ABNTNBR17225AcessibilidadeDigitalparaWeb.pdf) – Acessibilidade em conteúdo e aplicações web – Requisitos.
- ABNT. ABNT NBR 17060:2022 – Acessibilidade em aplicativos de dispositivos móveis – Requisitos.
- W3C. [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/). 2023.
- BRASIL. [eMAG – Modelo de Acessibilidade em Governo Eletrônico](https://emag.governoeletronico.gov.br/).

**Fontes internas do projeto**

- [Entrevista 01 – Profa. Adriana (PO)](../entrevistas/Entrevista01_Adriana.md), §3, §8, §11, §15, §32, §33.
- [Questionário 01 – Isabella](../questionarios/Questionario01_Isabella.md), RQ-01 a RQ-12.
- [Questionário 02 – Vaneide](../questionarios/Questionario02_Vaneide.md).
