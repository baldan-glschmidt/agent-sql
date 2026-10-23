# R128CUA

## Descrição

Cursos Aperfeiçoamento

---

## Resumo

- Campos: 49
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso |
| NomRed | String(060) | Sim | Nome Reduzido Curso |
| NomCua | String(200) | Sim | Nome do Curso |
| CodAss | Number(004,0) | Sim | Código do Assunto |
| ValCua | Number(003,0) | Sim | Validade do Curso em Meses |
| TipDur | Number(001,0) | Sim | Tipo de Duração |
| TemDur | Number(003,0) | Sim | Tempo de Duração |
| ChrCua | Number(010,0) | Sim | Carga Horária |
| FreCua | Number(005,2) | Sim | Percentual de Frequência Mínima Curso |
| MedCua | Number(005,2) | Sim | Média Mínima do Curso |
| TurCua | String(001) | Sim | Período do Curso |
| CodFlt | Number(003,0) | Sim | Código da Regra p/definição de Pré-Requisitos |
| DesCon | String(8001) | Sim | Descrição do Conteúdo |
| DesObu | String(2000) | Sim | Descrição do Objetivo |
| MetCua | String(1000) | Sim | Metodologia Curso |
| PubAlv | String(400) | Sim | Público Alvo |
| CodUsu | Number(010,0) | Sim | Identificação do Coordenador do Curso |
| ConRes | String(001) | Sim | Define se o curso estará disponível para reservas |
| PerRsv | String(001) | Sim | Permissão para efetuar a Reserva |
| TipRea | Number(003,0) | Sim | Tipo de Realização |
| TipCer | String(001) | Sim | Tipo do Certificado |
| RegExc | Number(003,0) | Sim | Regra de Exclusão de Participantes da Turma |
| RegSub | Number(003,0) | Sim | Regra de Substituição de Participantes da Turma |
| RegTrf | Number(003,0) | Sim | Regra de Transferência de Participante da Turma |
| NomArq | String(250) | Sim | Arquivo |
| TipCua | String(001) | Sim | Define se o curso é um Módulo (composto por outros cursos) |
| EmiCer | String(001) | Sim | Identifica se serão emitidos certificados para Disciplinas |
| ConWeb | String(001) | Sim | Considerar no preenchimento do Currículo Web |
| CodTst | String(005) | Sim | Código do questionário da avaliação de eficácia |
| IniEfi | Number(003,0) | Sim | Prazo em dias, para começar a avaliação de eficácia |
| PraAva | Number(003,0) | Sim | Prazo em dias, para ocorrer a avaliação de eficácia |
| PraARe | Number(003,0) | Sim | Prazo em dias, para ocorrer a avaliação de reação |
| ConPdi | String(001) | Sim | Define se este Curso é considerado no PDI |
| CriRep | Number(001,0) | Sim | Define se a reprovação será por média ou frequencia quando ambas estiverem abaixo do mínimo |
| RegInc | Number(003,0) | Sim | Regra de Inclusão de Participantes da Turma |
| ConFre | Number(001,0) | Sim | Define a forma de controlar a frequência do participante |
| RegCpl | Number(003,0) | Sim | Regra para complementar a avaliação do participante |
| DatExp | Date | Sim | Data de expiração do curso |
| CurTlt | Number(001,0) | Sim | Define se o curso é um TLT |
| AvaTlt | Number(001,0) | Sim | Define se o TLT terá avaliação |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| AbrLoc | String(1500) | Sim | Abrangência dos locais que utilizam o TLT |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração |
| DatAlt | Date | Sim | Data da última alteração |
| HorAlt | Number(005,0) | Sim | Hora da última alteração |
| MetEfi | Number(003,0) | Sim | Percentual mínimo para o evento ser considerado eficaz |
| DiaAnt | Number(003,0) | Sim | Quantidade de dias de antecipação para considerar o curso como pendente |
| CurRec | Number(009,0) | Sim | Código do Curso de Reciclagem |
| CodTce | Number(004,0) | Sim | Código do treinamento de acordo com tabela do eSocial |

---

## Chave Primária

- CodCua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R128CUA_019

**Tabela:** R140REA

| Origem | Destino |
|--------|---------|
| TipRea | TipRea |

