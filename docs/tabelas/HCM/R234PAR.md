# R234PAR

## Descrição

Evento - Participantes

---

## Resumo

- Campos: 27
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEvn | Number(009,0) | Não | Código do Evento |
| CodPes | Number(009,0) | Não | Código da Pessoa |
| NumEmp | Number(004,0) | Sim | Código da Empresa do Participante |
| EstPos | Number(003,0) | Sim | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Sim | Código do Posto de Trabalho em que o Colaborador atuará |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| CodCcu | String(018) | Sim | Código Centro Custo Contábil |
| ConEmi | String(001) | Sim | Convite Emitido |
| CerEmi | String(001) | Sim | Certificado Emitido |
| FreEmi | String(001) | Sim | Frequência Emitida |
| DatIns | Date | Sim | Data inscrição do participante |
| SitCua | Number(002,0) | Sim | Situação Histórico Curso Aperfeiçoamento |
| DatTer | Date | Sim | Data término do participante |
| DatCon | Date | Sim | Data de conclusão |
| QtdFal | Number(003,0) | Sim | Quantidade de Faltas |
| HorFal | Number(010,0) | Sim | Horas Faltas |
| TipCer | String(001) | Sim | Tipo do Certificado |
| NumCer | Number(005,0) | Sim | Número do Certificado |
| CodMin | Number(003,0) | Sim | Código do motivo de interrupção |
| SitAnt | Number(002,0) | Sim | Situação Anterior do Histórico Curso Aperfeiçoamento - Turma Cancelada |
| ComPIn | String(1600) | Sim | Comentário positivo do instrutor sobre o participante |
| ComNIn | String(1600) | Sim | Comentário negativo do instrutor sobre o participante |
| TemARE | String(001) | Sim | Avaliação de Reação gerada |
| MedCua | Number(005,2) | Sim | Média do Curso |
| FreCua | Number(005,2) | Sim | Frequência do Curso |
| EvnTra | Number(009,0) | Sim | Código do Evento em que foi transferido |

---

## Chave Primária

- CodEvn
- CodPes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R234PAR_000

**Tabela:** R234EVN

| Origem | Destino |
|--------|---------|
| CodEvn | CodEvn |

### IR_R234PAR_001

**Tabela:** R033PES

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |

### IR_R234PAR_006

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

