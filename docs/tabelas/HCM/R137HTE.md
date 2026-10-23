# R137HTE

## Descrição

Histórico de Solicitação de Teste

---

## Resumo

- Campos: 15
- Chave Primária: 2 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatSol | Date | Não | Data da solicitação do teste |
| SeqSol | Number(004,0) | Não | Sequência da solicitação |
| HorSol | Number(005,0) | Sim | Hora da solicitação |
| OriCan | Number(001,0) | Sim | Origem Candidato I,E |
| NumCan | Number(007,0) | Sim | Cadastro do Candidato Externo |
| NumEmp | Number(004,0) | Sim | Empresa |
| TipCol | Number(001,0) | Sim | Tipo do Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do Candidato Interno |
| CodUsu | Number(010,0) | Sim | Código do usuário que solicitou o teste |
| CodTes | Number(015,0) | Sim | Código do teste, atribuído pelo sistema MAP |
| DatCan | Date | Sim | Data em que a solicitação do teste foi cancelada |
| HorCan | Number(005,0) | Sim | Hora em que a solicitação de teste foi cancelada |
| UsuCan | Number(010,0) | Sim | Código do usuário que cancelou a solicitação |
| SitSol | Number(001,0) | Sim | Situação da solicitação(1-Solicitado/2-Cancelado) |
| SeqTes | Number(007,0) | Sim | Última sequência utilizada na solicitação de teste |

---

## Chave Primária

- DatSol
- SeqSol

---

## Índices

### R137HTEIndice2

**Tipo:** Não unico

Campos:
- NumCan

### R137HTEIndice3

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad

---

## Relacionamentos

Nenhum relacionamento cadastrado.
