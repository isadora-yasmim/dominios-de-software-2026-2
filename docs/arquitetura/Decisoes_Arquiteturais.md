# Decisões arquiteturais e stack tecnológica

**Projeto:** Sistema Web de Feedback e Gestão de Competências (Trilha) · **Etapa:** 2ª Entrega – Arquitetura e Desenho Detalhado
**Versão:** 1.0 · **Data:** 22/11/2026 · **Issue:** #80 · **Autora:** Isadora Yasmim da Silva · **Revisora:** Verônica Ribeiro Oliveira Palmeira

| Item | Descrição |
|---|---|
| Tipo e natureza | Registro de decisões arquiteturais (ADR, *Architecture Decision Record*), documento textual e prescritivo |
| Propósito | Fixar o estilo arquitetural, a stack tecnológica e os mecanismos de segurança, sessão e anonimato antes da modelagem dos níveis 1 a 4 do C4, para que DImp, DPac, DCmp, DCla, EOBD e contratos partam das mesmas premissas |
| Público-alvo | Integrantes do grupo (autores dos níveis N1 a N4 e das seções 3 e 4 do PDF) e a docente/PO |
| Uso no documento final | Base da justificativa dos mecanismos arquiteturais da seção 3 (#83) e do ambiente operacional da seção 4 (#84 a #86) |
| Identificadores | `ADR-01` a `ADR-14`. Toda referência a uma decisão, em qualquer artefato, usa esse ID |

---

## Sumário

1. [Formato dos registros](#1-formato-dos-registros)
2. [Visão geral da stack](#2-visão-geral-da-stack)
3. [Registros de decisão](#3-registros-de-decisão)
   - [ADR-01 – Estilo arquitetural](#adr-01--estilo-arquitetural-spa--api-rest-com-back-end-monolítico-modular-em-camadas)
   - [ADR-02 – Cliente web](#adr-02--cliente-web-spa-em-react-com-typescript)
   - [ADR-03 – Servidor web](#adr-03--servidor-web-nginx-como-proxy-reverso)
   - [ADR-04 – Servidor de aplicação](#adr-04--servidor-de-aplicação-java-com-spring-boot)
   - [ADR-05 – SGBD](#adr-05--sgbd-postgresql-com-esquemas-separados)
   - [ADR-06 – Notificações e rotinas automáticas](#adr-06--notificações-e-rotinas-automáticas-e-mail-por-smtp-com-caixa-de-saída)
   - [ADR-07 – Autenticação](#adr-07--autenticação-senha-e-segundo-fator-totp)
   - [ADR-08 – Sessão](#adr-08--sessão-no-servidor-com-cookie-opaco)
   - [ADR-09 – Autorização](#adr-09--autorização-por-perfil-e-por-escopo-do-registro)
   - [ADR-10 – Confidencialidade e anonimato](#adr-10--confidencialidade-e-anonimato-na-arquitetura)
   - [ADR-11 – Criptografia e chaves](#adr-11--criptografia-em-trânsito-em-repouso-e-gestão-de-chaves)
   - [ADR-12 – Auditoria e registros de acesso](#adr-12--trilha-de-auditoria-e-registros-de-acesso)
   - [ADR-13 – Sistemas externos](#adr-13--sistemas-externos-dentro-e-fora-desta-versão)
   - [ADR-14 – Hospedagem e implantação](#adr-14--hospedagem-e-implantação)
4. [Rastreabilidade decisão × requisito](#4-rastreabilidade-decisão--requisito)
5. [Impacto nos artefatos da 2ª etapa](#5-impacto-nos-artefatos-da-2ª-etapa)
6. [Pontos em aberto](#6-pontos-em-aberto)
7. [Referências](#7-referências)
8. [Histórico de revisões](#8-histórico-de-revisões)

---

## 1. Formato dos registros

Cada decisão segue o formato curto proposto por Nygard (2011), com um campo a mais para a rastreabilidade exigida pelo enunciado:

| Campo | Conteúdo |
|---|---|
| Situação | `Aceita` (vale para todos os artefatos), `Proposta` (aguarda o revisor) ou `Substituída por ADR-xx` |
| Contexto | Requisitos, regras e restrições que forçam a decisão |
| Decisão | O que foi escolhido, em uma ou poucas frases |
| Alternativas | Opções consideradas e por que foram descartadas |
| Consequências | Efeitos positivos, custos e riscos aceitos |
| Rastreabilidade | IDs dos requisitos (RF, RNF, RN), decisões anteriores (DS, M) e telas (T) relacionados |

Todas as decisões desta versão estão como **Proposta** até a aprovação do PR pela revisora. Depois do merge, passam a **Aceita**. Uma mudança posterior não edita o ADR: cria um novo, que o substitui.

---

## 2. Visão geral da stack

**Tabela 1 – Stack tecnológica por elemento do ambiente operacional.** Resume as escolhas detalhadas na seção 3; a coluna ADR indica onde está a justificativa.

| Elemento | Tecnologia escolhida | Papel | ADR |
|---|---|---|---|
| Estilo | SPA + API REST; back-end monolítico modular em camadas | Organização geral do sistema | ADR-01 |
| Cliente | Navegador (Chrome, Edge, Firefox, Safari) executando uma SPA em React + TypeScript | Interface responsiva e acessível | ADR-02 |
| Servidor web | Nginx | Terminação TLS, arquivos estáticos da SPA, proxy reverso para a API, cabeçalhos de segurança | ADR-03 |
| Servidor de aplicação | Java 21 (LTS) + Spring Boot 3, com Tomcat embutido | API REST, regras de negócio, autenticação, sessão, rotinas agendadas | ADR-04 |
| SGBD | PostgreSQL 17 | Dados do domínio, sessões, caixa de saída de e-mails, trilha de auditoria | ADR-05 |
| Notificação | Serviço de e-mail por SMTP (provedor contratado) + notificações internas | Lembretes e avisos (RF-026, RF-037, RF-040) | ADR-06 |
| Autenticação | E-mail e senha (Argon2id) + TOTP de 6 dígitos para RH e administrador | Login (T-01 a T-03) | ADR-07 |
| Sessão | Sessão no servidor, guardada no PostgreSQL, com cookie opaco `HttpOnly`, `Secure`, `SameSite=Strict` | Estado entre requisições | ADR-08 |
| Documentação da API | OpenAPI 3, gerada a partir do código | Contrato para a SPA e para o futuro aplicativo | ADR-01, ADR-04 |
| Implantação | Contêineres OCI em provedor de nuvem com região no Brasil | Ambiente de produção | ADR-14 |

---

## 3. Registros de decisão

### ADR-01 – Estilo arquitetural: SPA + API REST com back-end monolítico modular em camadas

**Situação:** Proposta

**Contexto.** O RNF-028 (Must) exige que toda funcionalidade esteja numa API independente da interface web, para que o futuro aplicativo móvel (RNF-035) reutilize as mesmas regras. O RNF-030 restringe o sistema a uma aplicação web acessada por navegador, e o RNF-027 pede interface responsiva. O porte é moderado: 500 colaboradores no cenário de referência, até 1.000 na meta de escalabilidade (DS-01, DS-04), uma organização por instalação (RN-010). O RNF-026 pede parametrização sem mudança de código, e a equipe tem tempo e tamanho de um projeto acadêmico.

**Decisão.** A interface é uma aplicação de página única (SPA) que se comunica com o back-end apenas por uma API REST com JSON, versionada no caminho (`/api/v1/...`) e descrita em OpenAPI 3. O back-end é um **monólito modular**: uma única unidade implantável, dividida em módulos de negócio com fronteiras explícitas, e cada módulo dividido em três camadas:

| Camada | Responsabilidade | Exemplo |
|---|---|---|
| Apresentação (API) | Recebe a requisição HTTP, valida o formato, converte JSON ↔ objetos, devolve status e erros no formato *Problem Details* (RFC 9457) | `FeedbackController` |
| Aplicação e domínio | Regras de negócio, autorização por escopo (ADR-09), transações | `FeedbackService`, `Feedback` |
| Persistência | Acesso ao banco por repositórios | `FeedbackRepository` |

Módulos propostos, alinhados às áreas do modelo ER (#52) e aos grupos de casos de uso; a lista definitiva é do DPac-01 (#90):

| Módulo | Área do modelo ER | Casos de uso |
|---|---|---|
| `organizacao` (organização, usuários e acesso) | Seção 4 | UC-01, UC-02 |
| `competencias` (competências e questionários) | Seção 5 | UC-03 a UC-05 |
| `feedback` (fatos, feedbacks e sessões) | Seção 6 | UC-06 a UC-12 |
| `avaliacao` (ciclos, convites e respostas) | Seções 7 e 8 (check-in) | UC-13 a UC-18 |
| `desenvolvimento` (metas, indicadores e planos de ação) | Seção 8 | UC-19 a UC-21 |
| `analise` (histórico e painéis) | Leitura das seções 6 a 8 | UC-22 a UC-24 |
| `privacidade` (LGPD, auditoria e notificações) | Seção 9 | UC-25 a UC-31 |

Um módulo só usa outro pela interface pública dele (serviços), nunca pelos repositórios ou tabelas do outro.

**Alternativas.**

| Alternativa | Motivo da rejeição |
|---|---|
| Aplicação de várias páginas com renderização no servidor (MPA/SSR) | Mistura interface e regra no mesmo código, o que contraria o item 2 do RNF-028 ("a interface web acessa os dados só pela API") |
| Microsserviços | Exigem infraestrutura de orquestração, comunicação entre serviços e transações distribuídas, sem ganho para o porte de 500 a 1.000 usuários. A escalabilidade do RNF-029 é atendida com réplicas do monólito (ADR-14) |
| GraphQL no lugar de REST | Menor familiaridade da equipe, e as seções 4.1 e 4.2 do PDF pedem a explicação de métodos, cabeçalhos e status HTTP, que o REST usa de forma direta |

**Consequências.**

- (+) Um único contrato (OpenAPI) atende à SPA e ao futuro aplicativo (RNF-028, RNF-035).
- (+) Implantação e testes simples; uma transação de banco cobre a regra de negócio, sem coordenação distribuída.
- (+) Os módulos com fronteiras explícitas permitem extrair um serviço no futuro, se necessário.
- (−) Todo o back-end escala junto. Aceito, porque a carga se concentra nas mesmas operações (RNF-009).
- (−) A SPA depende de JavaScript no navegador. Aceito, porque os navegadores do RNF-030 o suportam.

**Rastreabilidade:** RNF-026, RNF-027, RNF-028, RNF-029, RNF-030, RNF-035, RN-010, DS-01, DS-04.

---

### ADR-02 – Cliente web: SPA em React com TypeScript

**Situação:** Proposta

**Contexto.** A interface precisa ser responsiva (RNF-027), acessível nos níveis A e AA das WCAG 2.2 e na ABNT NBR 17225 (RNF-017 a RNF-023), em português (RNF-016), e salvar rascunhos automaticamente a cada campo (RNF-012). O protótipo (#50) já define 54 telas com componentes reutilizáveis (menu por perfil, cartões, campos, status).

**Decisão.** SPA em **React com TypeScript**, empacotada com Vite em arquivos estáticos servidos pelo Nginx (ADR-03). Diretrizes:

- componentes espelham a página Componentes do Figma;
- HTML semântico e atributo `lang="pt-BR"` (RNF-023);
- gráficos sempre com resumo textual e tabela equivalente (RNF-020, telas T-05 a T-07);
- formatação de datas e números com `Intl` em `pt-BR` (RNF-016);
- rascunho enviado à API a cada campo alterado (RNF-012); o navegador não guarda conteúdo de feedback em `localStorage`, para não deixar dado pessoal no computador (ADR-08);
- a SPA não contém regra de negócio que a API não aplique (RNF-028, item 2). Validações na tela são só conveniência; a API valida de novo.

**Alternativas.**

| Alternativa | Motivo da rejeição |
|---|---|
| Angular | Atende aos requisitos, mas é mais verboso e a equipe tem menos experiência com ele |
| Vue | Atende aos requisitos; preterido pela maior oferta de bibliotecas de componentes acessíveis e de material de estudo em React |
| Next.js (React com renderização no servidor) | Acrescenta um servidor Node.js à implantação sem necessidade: o sistema é de uso interno e não depende de indexação por buscadores |

**Consequências.**

- (+) Tipagem estática reduz erros na integração com a API; os tipos podem ser gerados do OpenAPI.
- (+) O mesmo conhecimento serve ao aplicativo móvel futuro, se for feito em React Native (RNF-035).
- (−) A acessibilidade depende de disciplina no desenvolvimento: a verificação dos RNF-017 a RNF-023 continua obrigatória em cada tela.

**Rastreabilidade:** RNF-012, RNF-016, RNF-017 a RNF-023, RNF-027, RNF-028, RNF-030, T-05 a T-07, T-48 a T-51.

---

### ADR-03 – Servidor web: Nginx como proxy reverso

**Situação:** Proposta

**Contexto.** Toda comunicação deve usar TLS 1.2 ou superior, recusando versões anteriores (RNF-004). A SPA é um conjunto de arquivos estáticos e a API roda no servidor de aplicação. O RNF-029 pede crescimento só com infraestrutura, o que implica poder ter mais de uma instância da API.

**Decisão.** O **Nginx** é o único ponto de entrada público e:

1. termina o TLS, com TLS 1.2 e 1.3 apenas, e redireciona HTTP (porta 80) para HTTPS (443);
2. serve os arquivos estáticos da SPA, com cache longo para arquivos com *hash* no nome;
3. encaminha `/api/` para as instâncias do servidor de aplicação (proxy reverso com balanceamento);
4. aplica cabeçalhos de segurança: `Strict-Transport-Security`, `Content-Security-Policy` restritiva, `X-Content-Type-Options: nosniff`, `Referrer-Policy: no-referrer`, `Permissions-Policy`;
5. limita a taxa de requisições nos endpoints de login, como primeira barreira contra tentativa e erro (a regra do RNF-006 fica na aplicação, ADR-07);
6. grava registros de acesso **sem** caminho completo nem corpo das requisições dos endpoints de resposta de avaliação (ADR-10, ADR-12).

**Alternativas.**

| Alternativa | Motivo da rejeição |
|---|---|
| Apache HTTP Server | Equivalente em função; o Nginx tem configuração de proxy reverso mais enxuta e menor consumo de memória por conexão |
| Expor o Tomcat diretamente | Deixa TLS, arquivos estáticos e cabeçalhos a cargo da aplicação e impede o balanceamento entre instâncias |
| Balanceador gerenciado do provedor de nuvem | Pode substituir os itens 1 e 3 na implantação; foi mantido o Nginx para que a arquitetura não dependa de um provedor específico |

**Consequências.**

- (+) A aplicação não lida com certificados; trocar ou renovar certificado não exige nova versão do software.
- (+) Separa as responsabilidades exigidas na seção 4.1 do PDF: servidor web (Nginx) e servidor de aplicação (Tomcat).
- (−) Mais um componente para configurar e monitorar.

**Rastreabilidade:** RNF-004, RNF-006, RNF-008, RNF-010, RNF-029, RNF-032.

---

### ADR-04 – Servidor de aplicação: Java com Spring Boot

**Situação:** Proposta

**Contexto.** O back-end concentra regras de negócio extensas (16 regras de negócio, autorização por perfil e por hierarquia), autenticação com dois fatores, sessão com limites de tempo (RNF-006), rotinas agendadas (UC-30, UC-31) e precisa publicar a API em OpenAPI (RNF-028).

**Decisão.** **Java 21 (LTS)** com **Spring Boot 3**, empacotado como JAR executável com **Tomcat embutido** como servidor de aplicação. Bibliotecas do ecossistema:

| Necessidade | Biblioteca |
|---|---|
| API REST e validação | Spring Web, Bean Validation |
| Autenticação, autorização, CSRF | Spring Security |
| Sessão guardada no banco | Spring Session JDBC |
| Persistência e migrações | Spring Data JPA (Hibernate) e Flyway |
| Rotinas agendadas | Agendador do Spring (`@Scheduled`), com trava no banco para rodar em uma só instância |
| Documentação OpenAPI | springdoc-openapi |
| Envio de e-mail | Spring Mail (SMTP) |

**Alternativas.**

| Alternativa | Motivo da rejeição |
|---|---|
| Node.js (NestJS) | Atende aos requisitos; preterido porque os mecanismos de sessão, CSRF e autorização por método exigiriam reunir bibliotecas de terceiros que o Spring Security já integra |
| Python (Django + DRF) | Atende aos requisitos; preterido pela familiaridade da equipe com Java na disciplina de orientação a objetos, o que facilita os DCla e os contratos de operação (N4) |
| Servidor de aplicação Jakarta EE externo (WildFly, Payara) | Exige instalar e administrar o servidor à parte; o Tomcat embutido basta, porque não há EJB nem transação distribuída |

**Consequências.**

- (+) Tipagem estática e orientação a objetos casam com os DCla e os contratos de operação da seção 5 (N4).
- (+) Flyway versiona o esquema do banco junto com o código, o que torna o EOBD (#102) rastreável a migrações.
- (−) Consumo de memória maior que alternativas em Node.js ou Go. Aceito para o porte previsto.

**Rastreabilidade:** RNF-006, RNF-026, RNF-028, RNF-029, RF-037, RF-040, RF-062.

---

### ADR-05 – SGBD: PostgreSQL com esquemas separados

**Situação:** Proposta

**Contexto.** O modelo ER (#52) é relacional, usa chaves `uuid` aleatórias (seção 10, mecanismo 3) e exige que o `VinculoConfidencial` fique em esquema separado, com acesso próprio (M-04, RNF-003). A trilha de auditoria é somente inclusão (RNF-005). Os dados devem ser criptografados em repouso (RNF-004) e os backups restaurados em até 4 h (RNF-011).

**Decisão.** **PostgreSQL 17**, com três esquemas e três papéis de banco:

| Esquema | Conteúdo | Papel que acessa | Permissões |
|---|---|---|---|
| `trilha` | Todas as entidades do domínio, sessões HTTP e caixa de saída de e-mails | `app` | Leitura e escrita |
| `confidencial` | `VinculoConfidencial` | `app_confidencial` (usado só pelo componente de vínculo confidencial, ADR-10) | Leitura e inclusão |
| `auditoria` | `RegistroAuditoria` | `app` | Somente `INSERT` e `SELECT`; `UPDATE`, `DELETE` e `TRUNCATE` revogados |

Tipos físicos de referência para o EOBD (#102): `uuid` para chaves (geradas aleatoriamente, versão 4), `timestamptz` para data e hora, `date` quando o modelo pede só a data (como `RespostaAvaliacao.data_envio`), `varchar(n)` com os tamanhos do dicionário de dados, `text` para textos livres, `bytea` para campos cifrados e enumerações como `varchar` com restrição `CHECK`.

**Alternativas.**

| Alternativa | Motivo da rejeição |
|---|---|
| MySQL/MariaDB | Não tem esquemas independentes dentro do mesmo banco com o mesmo nível de controle de permissões por papel, e tem suporte mais limitado a `uuid` nativo |
| Banco de documentos (MongoDB) | O domínio é fortemente relacional (hierarquia, ciclos, convites, respostas, metas), e a integridade referencial é necessária para o histórico (RN-003) |
| Banco separado só para o vínculo confidencial | Isolamento maior, mas exige dois servidores e backups coordenados. O esquema com papel próprio e chave de criptografia própria (ADR-11) atinge o objetivo do RNF-003 com menor custo |

**Consequências.**

- (+) O isolamento do vínculo é aplicado pelo banco, não só pelo código: o papel `app` não lê o esquema `confidencial`.
- (+) A revogação de `UPDATE` e `DELETE` na auditoria impede alterações pela aplicação, como pede o item 2 do RNF-005.
- (−) A aplicação abre dois *pools* de conexão, um por papel.

**Rastreabilidade:** RNF-003, RNF-004, RNF-005, RNF-011, RN-003, RN-004, M-04, seção 10 do modelo ER.

---

### ADR-06 – Notificações e rotinas automáticas: e-mail por SMTP com caixa de saída

**Situação:** Proposta

**Contexto.** Notificações e lembretes saem dentro do sistema e por e-mail (DS-10, RF-026, RF-037, RF-040). Rotinas automáticas (UC-30 e UC-31, ator Relógio do sistema) abrem e encerram ciclos, consolidam resultados (RF-032), enviam lembretes e aplicam a política de retenção (RF-062). Uma falha no provedor de e-mail não pode desfazer a ação do usuário que a disparou.

**Decisão.**

1. Notificações internas são registros da entidade `Notificacao`, lidas pela SPA na API.
2. E-mails seguem o padrão **caixa de saída transacional** (*transactional outbox*): a ação de negócio grava a mensagem numa tabela de saída na mesma transação; uma rotina agendada a envia por **SMTP com TLS** a um provedor de e-mail contratado e marca o envio, com novas tentativas em caso de falha.
3. As rotinas automáticas rodam no agendador do Spring (ADR-04), com trava no banco para que só uma instância execute cada rotina.
4. Os e-mails não levam conteúdo de feedback nem identidade de emissor: só o aviso e o link para o sistema (por exemplo, "Você recebeu um feedback").

**Alternativas.**

| Alternativa | Motivo da rejeição |
|---|---|
| Envio síncrono durante a requisição | Atrasa a resposta (RNF-008) e faz a ação falhar se o provedor estiver fora |
| Fila de mensagens dedicada (RabbitMQ, Kafka) | Mais um componente para operar, sem necessidade no volume previsto; a tabela de saída dá a mesma garantia de entrega |
| WhatsApp ou outros aplicativos de mensagem | Integração externa não pedida (DS-10, C-11) |

**Consequências.**

- (+) A ação do usuário e o registro da notificação são atômicos; o e-mail é entregue ao menos uma vez.
- (+) Sem conteúdo sensível no e-mail, a caixa postal do colaborador não vira cópia de dados de feedback.
- (−) O e-mail pode chegar com atraso de alguns minutos. Aceito, porque os lembretes têm antecedência de horas ou dias.
- (−) O provedor de e-mail trata dados pessoais (nome e e-mail): exige contrato de operador e, se for fora do Brasil, o mecanismo do RNF-033.

**Rastreabilidade:** RF-026, RF-032, RF-037, RF-040, RF-062, RNF-008, RNF-033, DS-10, C-11.

---

### ADR-07 – Autenticação: senha e segundo fator TOTP

**Situação:** Proposta

**Contexto.** O protótipo define login com e-mail corporativo e senha, que aceita colar e gerenciador de senhas (T-01, RNF-022), mensagem de erro (T-03, RNF-021) e verificação em duas etapas com **código de 6 dígitos de aplicativo autenticador** e opção de **código de recuperação** para RH e administrador (T-02). O RNF-006 exige dois fatores para esses perfis, espera crescente de 30 s a 1 h após falhas e desativação do autenticador em 100 falhas consecutivas (DS-06). O login único (RF-004) está fora desta versão. O modelo ER já tem `senha_hash`, `falhas_login_consecutivas` e `login_bloqueado_ate` em `Colaborador`.

**Decisão.**

1. **Primeiro fator:** e-mail e senha. A senha é guardada com **Argon2id** e sal aleatório. Mínimo de 8 caracteres sem regras de composição, com verificação contra lista de senhas vazadas, conforme NIST SP 800-63B-4. Os campos aceitam colar e preenchimento automático (`autocomplete="current-password"`).
2. **Segundo fator:** **TOTP** (RFC 6238), 6 dígitos, janela de 30 s, obrigatório para quem tem perfil RH ou administrador, inclusive quando o perfil é acumulado (RF-003). O segredo é guardado cifrado (ADR-11). No cadastro do autenticador são gerados **10 códigos de recuperação** de uso único, guardados como *hash*.
3. **Limitação de tentativas:** contagem de falhas por conta, espera crescente de 30 s até 1 h e desativação do autenticador em 100 falhas, conforme DS-06. A mensagem de erro não revela se o e-mail existe (T-03).
4. **Redefinição de senha:** por link de uso único enviado ao e-mail cadastrado, válido por 1 h. Para RH e administrador, a redefinição também exige o segundo fator ou um código de recuperação.
5. O fluxo de primeiro acesso (T-04) é exibido depois da autenticação, uma vez por versão do aviso de privacidade.

**Alternativas.**

| Alternativa | Motivo da rejeição |
|---|---|
| Código por SMS | O NIST classifica o SMS como autenticador restrito, sujeito a troca de chip; e o protótipo já mostra aplicativo autenticador (T-02) |
| Código por e-mail como segundo fator | Se a senha do e-mail corporativo for a mesma, os dois fatores caem juntos |
| Chaves de acesso (*passkeys*, WebAuthn) | Mais resistentes a *phishing*, mas exigem dispositivo compatível de todos os usuários de RH e administração; ficam como evolução |
| Bloqueio da conta após poucas tentativas | Permite que alguém bloqueie a conta de outra pessoa de propósito (DS-06) |

**Consequências.**

- (+) Coerente com as telas T-01 a T-04 e com o NIST SP 800-63B-4 (AAL2 para RH e administrador).
- (+) A camada de autenticação fica atrás de uma interface no módulo `organizacao`, o que permite acrescentar SSO (RF-004) depois sem mudar os outros módulos (ADR-13).
- (−) O modelo ER e o dicionário de dados não têm atributos para o segredo TOTP nem para os códigos de recuperação: precisam ser acrescentados no ECBD/EOBD (seção 5).

**Rastreabilidade:** RF-003, RF-004, RF-053, RNF-006, RNF-021, RNF-022, DS-05, DS-06, T-01, T-02, T-03, T-04.

---

### ADR-08 – Sessão no servidor com cookie opaco

**Situação:** Proposta

**Contexto.** HTTP não guarda estado; a seção 4.3 do PDF (#86) pede o mecanismo de sessão. O RNF-006 e a DS-05 exigem encerrar a sessão após 1 h de inatividade e 24 h de duração total, para todos os perfis. A sessão precisa funcionar com mais de uma instância da API (RNF-029) e poder ser revogada, por exemplo quando o colaborador é desligado ou troca a senha. O conteúdo de feedback é dado pessoal de duas pessoas (seção 8 da especificação suplementar), e um *script* malicioso na página não pode roubar a sessão.

**Decisão.**

1. Depois da autenticação (ADR-07), o servidor cria uma sessão e devolve um **identificador aleatório e opaco** num cookie `SESSION` com `HttpOnly`, `Secure`, `SameSite=Strict` e `Path=/api`. O identificador é trocado a cada login e a cada elevação de privilégio (fixação de sessão).
2. Os dados da sessão (usuário, perfis, momento de criação e de último acesso, segundo fator concluído) ficam no **PostgreSQL**, pelo Spring Session JDBC, e não no navegador.
3. A cada requisição, o servidor verifica os dois limites: inatividade maior que 1 h ou duração total maior que 24 h encerram a sessão e devolvem `401 Unauthorized`. A SPA então leva à tela de login, e o rascunho já salvo no servidor é recuperado depois (RNF-012).
4. Proteção contra CSRF: além do `SameSite=Strict`, toda requisição que altera estado (`POST`, `PUT`, `PATCH`, `DELETE`) leva um *token* CSRF num cabeçalho (`X-XSRF-TOKEN`), conferido pelo Spring Security.
5. Sair (logout) apaga a sessão no banco. Desligar o colaborador, trocar a senha ou desativar o autenticador apaga todas as sessões dele.
6. Para o futuro aplicativo móvel (RNF-035), que não usa cookie, a mesma sessão será entregue como *token* opaco no cabeçalho `Authorization: Bearer`, sem mudar o armazenamento nem as regras.

**Alternativas.**

| Alternativa | Motivo da rejeição |
|---|---|
| JWT sem estado guardado no `localStorage` | Lido por qualquer *script* da página (risco de XSS) e não pode ser revogado antes de expirar, o que dificulta encerrar a sessão do colaborador desligado |
| JWT em cookie `HttpOnly` | Resolve o XSS, mas continua sem revogação imediata; o controle de inatividade exigiria guardar estado no servidor de qualquer forma |
| Sessão na memória do Tomcat | Perde-se a sessão ao reiniciar e prende o usuário a uma instância, o que dificulta o RNF-029 |
| Redis para as sessões | Mais rápido, mas é mais um componente; com 1.000 usuários simultâneos o PostgreSQL atende, e a troca para Redis no futuro não muda o código de negócio |

**Consequências.**

- (+) Limites de tempo e revogação controlados no servidor, como pede o RNF-006.
- (+) Qualquer instância atende a qualquer requisição (escala horizontal, RNF-029).
- (−) Uma leitura no banco por requisição. Aceito para o porte; os índices da tabela de sessões entram no EOBD.
- (−) A SPA e a API precisam estar no mesmo domínio (o Nginx serve as duas, ADR-03) para o cookie `SameSite=Strict` funcionar.

**Rastreabilidade:** RNF-001, RNF-006, RNF-012, RNF-028, RNF-029, RNF-035, DS-05.

---

### ADR-09 – Autorização por perfil e por escopo do registro

**Situação:** Proposta

**Contexto.** A matriz da seção 8.1 da especificação suplementar define o que cada perfil vê, e a visibilidade depende da relação com o registro: o gestor vê só a sua equipe, o emissor só o que escreveu, o RH não consulta a identidade de quem o avaliou (RN-004). A negação vale também para chamadas diretas à API com identificadores de outro colaborador (RNF-001, item 2). Um usuário acumula perfis (RF-003).

**Decisão.** A autorização tem dois níveis, ambos no back-end:

1. **Por perfil (RBAC):** cada endpoint declara os perfis que podem chamá-lo, verificado pelo Spring Security antes do controlador.
2. **Por escopo do registro:** a camada de aplicação de cada módulo verifica a relação entre o usuário e o registro pedido (próprio, equipe pela hierarquia `gestor_id`, organização) antes de devolvê-lo, e filtra as consultas de lista pelo mesmo critério. Registro fora do escopo devolve `404 Not Found`, para não confirmar que o identificador existe.

A SPA esconde menus e botões conforme o perfil apenas por usabilidade; isso não é controle de acesso.

**Alternativas.**

| Alternativa | Motivo da rejeição |
|---|---|
| Só RBAC | Não distingue "o gestor desta equipe" de "um gestor qualquer", o que viola o RNF-001 |
| Segurança por linha no banco (*row-level security*) para todo o domínio | Desloca regra de negócio para o banco e dificulta testar e documentar nos DSeq; fica restrita ao esquema `confidencial` (ADR-05) |
| Controle de acesso por atributos com motor externo (OPA, por exemplo) | Mais um componente e uma linguagem de política para o porte do sistema |

**Consequências.**

- (+) Os testes de autorização do RNF-001 podem ser escritos por perfil e por escopo, pela interface e pela API.
- (−) Cada caso de uso precisa explicitar a regra de escopo; os contratos de operação (#105) registram isso como pré-condição.

**Rastreabilidade:** RF-003, RNF-001, RNF-002, RN-004, RN-005, RN-006, seção 8.1 da especificação suplementar.

---

### ADR-10 – Confidencialidade e anonimato na arquitetura

**Situação:** Proposta

**Contexto.** A RN-004 define três modos de identificação do emissor. A seção 8.3 da especificação suplementar e a seção 10 do modelo ER já resolvem a desvinculação **nos dados** (convite e resposta sem chave em comum, só a data do envio, `uuid` aleatório, rascunho preso ao convite, exibição agregada com mínimo de respondentes). Falta garantir que os **demais componentes** não reconstruam o vínculo que o modelo removeu: registros de acesso do Nginx, registros da aplicação, trilha de auditoria, ordem das transações e a própria sessão sabem quem está enviando a resposta.

**Decisão.** As respostas de avaliação e os feedbacks nos modos confidencial e anônimo passam por um caminho próprio, com estas regras:

| # | Mecanismo | Modo | Onde atua |
|---|---|---|---|
| 1 | O conteúdo é gravado sem `avaliador_id`/`emissor_id`. No modo confidencial, o vínculo é gravado por um componente próprio (`VinculoConfidencial`), que usa o papel de banco `app_confidencial` e chave de criptografia própria (ADR-05, ADR-11). No modo anônimo, nenhum vínculo é criado | Confidencial e anônimo | Back-end, banco |
| 2 | A marcação do convite como `RESPONDIDO` e a gravação da resposta ocorrem em transações separadas. A resposta não guarda horário, só a data | Anônimo | Back-end |
| 3 | Os registros da aplicação nunca contêm o identificador do usuário junto com o identificador ou o conteúdo de uma resposta; os registros de SQL do banco ficam desligados em produção | Confidencial e anônimo | Back-end, banco |
| 4 | O Nginx registra os endpoints de envio de resposta sem caminho completo, sem corpo e sem o identificador da sessão (ADR-03); o registro de acesso exigido pelo Marco Civil fica no nível do login e da sessão (ADR-12) | Anônimo | Servidor web |
| 5 | A trilha de auditoria registra "convite respondido" ligado ao convite, sem o identificador da resposta; a criação da resposta anônima é registrada sem ator | Anônimo | Auditoria |
| 6 | Toda leitura do vínculo confidencial passa por um único serviço, que só aceita o perfil RH, recusa quando o usuário RH é o avaliado (RN-004) e grava `CONSULTA_IDENTIDADE` na auditoria antes de devolver o dado | Confidencial | Back-end |
| 7 | A API do avaliado devolve só `ResultadoConsolidado`, calculado ao encerrar o ciclo (M-08), aplicando o mínimo de respondentes (RN-005, padrão 3); `ItemResposta` de modalidades não identificadas não tem endpoint de leitura para o avaliado, o gestor ou a diretoria | Confidencial e anônimo | Back-end |
| 8 | A palavra "anônimo" só aparece na interface quando o modo é anônimo; nos demais, a SPA exibe o aviso do RF-019 com quem pode ver a identidade | Todos | Cliente |

**Alternativas.**

| Alternativa | Motivo da rejeição |
|---|---|
| Confiar só no modelo de dados | Os registros do Nginx e da aplicação guardariam usuário e horário de cada envio, o que permite reidentificar por correlação (risco apontado pela ANPD; DS-12) |
| Enviar a resposta anônima sem sessão (por *token* de uso único do convite) | Esconde o usuário da requisição, mas o *token* liga convite e resposta e precisa ser guardado; a separação de transações e registros tem o mesmo efeito sem criar novo vínculo |
| Atrasar e embaralhar o envio das respostas em lote | Reduz ainda mais a correlação por tempo, mas atrasa a confirmação ao usuário (RNF-008) e complica a consolidação; fica como melhoria se o teste de reidentificação da seção 8.3 apontar risco |

**Consequências.**

- (+) A desvinculação vale em todas as camadas, não só no banco, e pode ser verificada pelo teste de reidentificação previsto na seção 8.3 da especificação suplementar.
- (−) No modo anônimo, o emissor não edita a resposta depois do envio (consequência já aceita na seção 10 do modelo ER).
- (−) Risco residual aceito: quem tem acesso administrativo direto ao servidor de banco poderia correlacionar a ordem física de gravação. Mitigado pelo acesso restrito à infraestrutura, pela auditoria do provedor e pelo registro em contrato.
- (−) Os DSeq de responder avaliação (UC-14) devem mostrar as duas transações separadas e o componente de vínculo confidencial.

**Rastreabilidade:** RN-004, RN-005, RNF-001, RNF-003, RNF-005, RF-019, RF-029, RF-032, DS-12, M-04, M-08, seção 10 do modelo ER, seção 8.3 da especificação suplementar, T-14 a T-19.

---

### ADR-11 – Criptografia em trânsito, em repouso e gestão de chaves

**Situação:** Proposta

**Contexto.** O RNF-004 exige TLS 1.2 ou superior e criptografia em repouso de banco, arquivos e backups. O RNF-003 exige controle de acesso próprio para o vínculo confidencial, e o modelo ER prevê chave de criptografia própria para ele e o campo `ConviteAvaliacao.rascunho_cifrado`.

**Decisão.**

| Camada | Mecanismo |
|---|---|
| Em trânsito, navegador ↔ Nginx | TLS 1.2 e 1.3 (ADR-03) |
| Em trânsito, Nginx ↔ aplicação ↔ banco ↔ SMTP | TLS na rede interna do provedor e no envio ao provedor de e-mail |
| Em repouso, disco do banco e backups | Criptografia de volume com AES-256, gerenciada pelo provedor; backups cifrados antes da cópia para outro local |
| Em repouso, campos sensíveis | Criptografia na aplicação com AES-256-GCM: `VinculoConfidencial` (chave `K_vinculo`), `rascunho_cifrado` e segredo TOTP (chave `K_dados`) |
| Senhas e códigos de recuperação | *Hash* Argon2id, não reversível (ADR-07) |

As chaves `K_vinculo` e `K_dados` ficam no cofre de segredos do provedor de nuvem, fora do banco e do código, e são entregues ao contêiner da aplicação em tempo de execução. Só o componente de vínculo confidencial recebe `K_vinculo`. A rotação é anual ou após incidente, com regravação dos campos.

**Alternativas.**

| Alternativa | Motivo da rejeição |
|---|---|
| Só criptografia de volume | Protege contra roubo do disco, mas quem acessa o banco com o papel `app` leria o vínculo em claro |
| Extensão `pgcrypto` com a chave enviada nas consultas | A chave transita nas consultas e pode aparecer em registros do banco |
| Chaves em arquivo de configuração no repositório | Exposição no controle de versão |

**Consequências.**

- (+) O vínculo confidencial exige duas barreiras: o papel `app_confidencial` e a chave `K_vinculo`.
- (−) Campos cifrados não podem ser pesquisados nem indexados pelo conteúdo. Aceito: nenhum caso de uso busca pelo vínculo ou pelo rascunho.
- (−) Perder a chave torna o dado ilegível; o cofre de segredos precisa de cópia de segurança própria, coberta pelo RNF-011.

**Rastreabilidade:** RNF-003, RNF-004, RNF-011, RNF-034, seção 10 do modelo ER.

---

### ADR-12 – Trilha de auditoria e registros de acesso

**Situação:** Proposta

**Contexto.** O RNF-005 pede trilha inalterável (quem, quando, o quê, de onde), detecção de alteração fora da aplicação e registro de toda consulta à identidade de emissor confidencial. O RNF-032 exige, se o sistema for operado como serviço, a guarda dos registros de acesso (data, hora e IP) por 6 meses (Marco Civil, art. 15). O ADR-10 impede que esses registros reidentifiquem respostas anônimas.

**Decisão.**

1. **Trilha de auditoria** no esquema `auditoria` (ADR-05), somente inclusão, com cada registro guardando o *hash* SHA-256 do anterior (`hash_anterior`, já previsto no modelo ER). Uma rotina diária verifica a cadeia e alerta o administrador se houver quebra.
2. A gravação na trilha é feita na mesma transação da ação auditada; se a gravação falhar, a ação é desfeita.
3. **Registro de acesso do Marco Civil:** login, logout e expiração de sessão, com usuário, data, hora e IP, guardados por no mínimo 6 meses. Não é feito por endpoint, para respeitar o ADR-10.
4. **Registros técnicos** (Nginx e aplicação) servem para diagnóstico, não contêm conteúdo de feedback e são guardados por 30 dias.

**Alternativas.**

| Alternativa | Motivo da rejeição |
|---|---|
| Trilha só nos registros de texto da aplicação | Alteráveis por quem acessa o servidor e difíceis de consultar |
| Serviço externo de registros imutáveis | Mais um operador de dados pessoais e mais uma transferência a contratar (RNF-033); fica como evolução |

**Consequências.**

- (+) O DSeq de consultar identidade confidencial mostra a gravação na auditoria antes da resposta, como exige o RNF-003.
- (−) A cadeia de *hash* serializa as inclusões na trilha. Aceito para o volume previsto.

**Rastreabilidade:** RNF-003, RNF-005, RNF-032, RF-062, RF-063, seção 9 do modelo ER.

---

### ADR-13 – Sistemas externos dentro e fora desta versão

**Situação:** Proposta

**Contexto.** A PO aceitou importação por planilha ou cadastro manual no lugar de integração com RH (E01 §30). O SSO (RF-004) e a API de RH (RNF-025) são Won't (C-11). O atalho para o canal de denúncias (RF-064, RN-009) aponta para um sistema da organização. Os diagramas de contexto (N1) e os DSeq precisam listar os mesmos sistemas externos (checklist do Apêndice 2 do enunciado).

**Decisão.**

| Sistema externo | Situação nesta versão | Forma de ligação | Preparação para o futuro |
|---|---|---|---|
| Serviço de e-mail (SMTP) | **Dentro** | SMTP com TLS, saída (ADR-06) | — |
| Canal de denúncias da organização | **Dentro**, só como link | Hiperlink configurado pelo administrador; nenhum dado é trocado | — |
| Sistemas de RH e folha de pagamento | **Fora** (RNF-025, Won't) | Substituído por importação CSV (RF-002) | O módulo `organizacao` recebe os dados por um serviço de importação; uma API de RH futura chamará o mesmo serviço |
| Provedor de identidade da organização (SSO) | **Fora** (RF-004, Won't) | Substituído por login próprio (ADR-07) | A autenticação fica atrás de uma interface; um provedor OpenID Connect pode ser acrescentado sem mudar os outros módulos |
| Aplicativos de mensagem (WhatsApp) e agenda corporativa | **Fora** (DS-10, C-11) | — | Novos canais entram como implementações do envio de notificação |

As sugestões de horários livres da tela de sessão de feedback (T-46) são calculadas com as sessões já agendadas no próprio sistema, sem consultar agenda externa.

**Consequências.**

- (+) O DImp-01 e os DSeq têm exatamente dois sistemas externos com que se comunicam ou para onde levam o usuário: serviço de e-mail e canal de denúncias.
- (−) A atualização de colaboradores depende de importações periódicas pelo RH até existir a integração.

**Rastreabilidade:** RF-002, RF-004, RF-064, RNF-025, RN-009, DS-10, C-11, T-01, T-46.

---

### ADR-14 – Hospedagem e implantação

**Situação:** Proposta

**Contexto.** Disponibilidade de 99,5% ao mês (RNF-010), RPO de 24 h e RTO de 4 h (RNF-011), escala só com infraestrutura (RNF-029), transferência internacional apenas com mecanismo do art. 33 da LGPD (RNF-033) e documentação de fluxo de dados para o RIPD (RNF-034).

**Decisão.**

1. Nginx, aplicação e rotinas são empacotados em **contêineres OCI** e implantados em provedor de nuvem com **região no Brasil**. O PostgreSQL usa o serviço gerenciado do mesmo provedor, na mesma região.
2. Produção começa com **duas instâncias** da aplicação atrás do Nginx, para tolerar a falha de uma e permitir atualização sem parada; mais instâncias são acrescentadas para o RNF-029.
3. Backup completo diário e registro contínuo de transações (*point-in-time recovery*), cifrados, com cópia em outra zona da mesma região; teste de restauração antes de cada ciclo formal (DS-08).
4. Monitoramento externo a cada minuto do login e da API (RNF-010, item 1).
5. Ambientes de desenvolvimento, homologação e produção separados; dados reais só em produção.

**Alternativas.**

| Alternativa | Motivo da rejeição |
|---|---|
| Servidor próprio da organização (*on-premises*) | Possível, mas exige que a organização opere backup, monitoramento e disponibilidade; a arquitetura em contêineres permite essa opção sem mudança de código |
| Região fora do Brasil | Exige cláusulas-padrão da ANPD (RNF-033) e aviso no RF-053, sem ganho técnico |

**Consequências.**

- (+) Sem transferência internacional dos dados do banco; o RNF-033 só se aplica ao provedor de e-mail, se for estrangeiro (ADR-06).
- (−) Custo de duas instâncias e de banco gerenciado. Aceito pela meta de disponibilidade.

**Rastreabilidade:** RNF-010, RNF-011, RNF-029, RNF-032, RNF-033, RNF-034, DS-08, DS-09.

---

## 4. Rastreabilidade decisão × requisito

**Tabela 2 – Requisitos não funcionais e regras atendidos por cada decisão.** Usada pela seção 3 do PDF (#83) para justificar os mecanismos arquiteturais e pela matriz da arquitetura (#106).

| Requisito | Característica ISO/IEC 25010 | Decisões |
|---|---|---|
| RNF-001, RNF-002 | Segurança – confidencialidade | ADR-08, ADR-09, ADR-10 |
| RNF-003 | Segurança – confidencialidade, responsabilização | ADR-05, ADR-10, ADR-11, ADR-12 |
| RNF-004 | Segurança – confidencialidade, integridade | ADR-03, ADR-11 |
| RNF-005 | Segurança – responsabilização, não repúdio | ADR-05, ADR-12 |
| RNF-006 | Segurança – autenticidade, resistência | ADR-07, ADR-08 |
| RNF-008, RNF-009 | Eficiência de desempenho | ADR-01, ADR-03, ADR-06 |
| RNF-010, RNF-011 | Confiabilidade | ADR-11, ADR-14 |
| RNF-012 | Confiabilidade – tolerância a falhas | ADR-02, ADR-08 |
| RNF-016 a RNF-023 | Capacidade de interação | ADR-02 |
| RNF-025, RF-004 | Compatibilidade (fora desta versão) | ADR-13 |
| RNF-026 | Manutenibilidade – modificabilidade | ADR-01, ADR-04 |
| RNF-027, RNF-030 | Flexibilidade, restrição de plataforma | ADR-01, ADR-02 |
| RNF-028, RNF-035 | Flexibilidade, manutenibilidade | ADR-01, ADR-08 |
| RNF-029 | Flexibilidade – escalabilidade | ADR-01, ADR-03, ADR-08, ADR-14 |
| RNF-032, RNF-033, RNF-034 | Restrições legais | ADR-06, ADR-12, ADR-14 |
| RN-004, RN-005 | Regras de negócio (anonimato) | ADR-09, ADR-10 |

---

## 5. Impacto nos artefatos da 2ª etapa

| Artefato (issue) | O que deve refletir destas decisões |
|---|---|
| Seções 3 e 4 do PDF (#83 a #86) | Mecanismos justificados pelos ADR (Tabela 2); servidor web = Nginx, servidor de aplicação = Tomcat embutido no Spring Boot; sessão por cookie opaco (ADR-08); status de erro conforme ADR-01 e ADR-09 |
| DImp-01 (#87) | Nós: navegador, Nginx, contêineres da aplicação (2 instâncias), PostgreSQL gerenciado, cofre de segredos; sistemas externos: serviço de e-mail e canal de denúncias (ADR-13). O banco aparece com os esquemas `trilha`, `confidencial` e `auditoria` |
| DPac-01 (#90) | Pacotes da SPA e do back-end, com os módulos do ADR-01 e as camadas apresentação, aplicação/domínio e persistência |
| DCmp (#97, #98) | Componente de vínculo confidencial separado (ADR-10); componentes de autenticação e sessão (ADR-07, ADR-08); caixa de saída de e-mails e agendador (ADR-06); auditoria (ADR-12) |
| ECBD e EOBD (#99, #102) | Acrescentar ao modelo: segredo TOTP cifrado, indicador de segundo fator ativo e códigos de recuperação em *hash* (ADR-07); tabela de sessões do Spring Session (ADR-08); tabela de saída de e-mails (ADR-06); tipos físicos do ADR-05. Registrar esses acréscimos como inconsistência resolvida no dicionário de dados |
| DSeq entre componentes (#100, #101) | Autenticação com segundo fator, expiração de sessão, resposta anônima em duas transações e consulta à identidade confidencial com auditoria |
| DCla, DSeq de operações e contratos (#103 a #105) | Exceções com status HTTP do ADR-01 (*Problem Details*) e do ADR-09 (`404` para registro fora do escopo, `401` para sessão expirada, `403` para perfil sem permissão) |

---

## 6. Pontos em aberto

| # | Ponto | Encaminhamento |
|---|---|---|
| A-01 | Escolha do provedor de nuvem e do provedor de e-mail | Não muda a arquitetura; fica para a implantação. Restrição: região no Brasil ou mecanismo do RNF-033 |
| A-02 | Confirmar com a PO a DS-10 (e-mail como canal de notificação), da qual depende o ADR-06 | Levar à próxima reunião com a docente/PO |
| A-03 | Passkeys (WebAuthn) como segundo fator alternativo | Evolução; não exige mudar o ADR-08 |

---

## 7. Referências

**Arquitetura e segurança**

- NYGARD, M. [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions). 2011. Formato dos ADR.
- LARMAN, C. *Utilizando UML e Padrões: uma introdução à análise e ao projeto orientados a objetos e ao desenvolvimento iterativo*. 3. ed. Porto Alegre: Bookman, 2007. Cap. 13 (arquitetura lógica em camadas).
- NIST. [SP 800-63B-4 – Digital Identity Guidelines: Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html). 2025. Senhas, autenticadores, limitação de tentativas e sessão.
- IETF. [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238) – TOTP: Time-Based One-Time Password Algorithm. 2011.
- IETF. [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457) – Problem Details for HTTP APIs. 2023.
- IETF. [RFC 6265](https://www.rfc-editor.org/rfc/rfc6265) – HTTP State Management Mechanism (cookies). 2011.
- OWASP. [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) e [Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html).
- RICHARDSON, C. [Pattern: Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html).
- OpenAPI Initiative. [OpenAPI Specification](https://spec.openapis.org/oas/latest.html).

**Legislação**

- BRASIL. [Lei nº 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) – LGPD, arts. 33, 46 e 48.
- BRASIL. [Lei nº 12.965/2014](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm) – Marco Civil da Internet, art. 15.

**Fontes internas do projeto**

- [Lista Geral de Requisitos](../Lista_Geral_Requisitos.md) (#45): RN-004, RN-005, RF-004, conflito C-11.
- [Especificação Suplementar](../Especificacao_Suplementar.md) (#51): seções 8, 10, 12, 13 e 15 (DS-05, DS-06, DS-08, DS-10, DS-12).
- [Modelo de domínio e ER](../modelagem/modelo-dados/Modelo_Dominio_ER.md) (#52): seções 9, 10 e 13 (M-04, M-08).
- [Dicionário de dados](../Dicionario_de_Dados.md) (#53).
- [Protótipo](../prototipacao/Prototipo.md) (#50): telas T-01 a T-04, T-14 a T-19 e T-46.

**Uso de inteligência artificial**

- ANTHROPIC. Claude Code (modelo Claude Opus 5.5). Disponível em: https://claude.com/claude-code. Acesso em: 22 nov. 2026. Usado para redigir a primeira versão deste documento a partir da issue #80 e dos artefatos da 1ª etapa. Questão: Apêndice II, Seção II.3 (issue #107).

---

## 8. Histórico de revisões

| Versão | Data | Autor(a) | Alteração |
|---|---|---|---|
| 1.0 | 22/11/2026 | Isadora Yasmim da Silva | Versão inicial: stack tecnológica e ADR-01 a ADR-14 (issue #80) |
