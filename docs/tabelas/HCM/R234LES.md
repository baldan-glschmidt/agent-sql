# R234LES

## Descrição

Evento - Lista de espera

---

## Resumo

- Campos: 18
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEvn | Number(009,0) | Não | Código do Evento |
| CodPes | Number(009,0) | Não | Código da Pessoa |
| SitLes | Number(001,0) | Sim | Indica a Situação da Pessoa na Lista de Espera |
| CodPri | Number(003,0) | Sim | Código de Prioridade da Pessoa |
| DatIns | Date | Sim | Data de Inscrição da Pessoa na Lista de Espera |
| HorIns | Number(005,0) | Sim | Hora Inscrição da Pessoa na Lista de Espera |
| OriLes | Number(001,0) | Sim | Origem da Inscrição na Lista de Espera |
| CodUsu | Number(010,0) | Sim | Código Usuário Responsável pela Inscrição |
| EveCnf | Number(009,0) | Sim | Código do Evento em que foi confirmado |
| SitCon | Number(001,0) | Sim | Define a Situação do Convite |
| DatAce | Date | Sim | Data de Aceite do Convite |
| HorAce | Number(005,0) | Sim | Hora de Aceite do Convite |
| NumEmp | Number(004,0) | Sim | Código da Empresa do Participante |
| EstPos | Number(003,0) | Sim | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Sim | Código do Posto de Trabalho em que o Colaborador atuará |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| CodCcu | String(018) | Sim | Código Centro Custo Contábil |

---

## Chave Primária

- CodEvn
- CodPes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R234LES_000

**Tabela:** R234EVN

| Origem | Destino |
|--------|---------|
| CodEvn | CodEvn |

### IR_R234LES_001

**Tabela:** R033PES

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |

### IR_R234LES_016

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

