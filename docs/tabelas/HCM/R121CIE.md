# R121CIE

## Descrição

Concurso - Etapas Realizadas Candidato Interno

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| AnoCon | Number(004,0) | Não | Ano para controle de identificação do concurso |
| NumCon | Number(006,0) | Não | Número do Concurso |
| NumEmp | Number(004,0) | Não | Empresa do candidato |
| TipCol | Number(001,0) | Não | Tipo do candidato |
| NumCad | Number(009,0) | Não | Cadastro do candidato |
| CodEta | Number(003,0) | Não | Código da Etapa |
| DatRea | Date | Sim | Data de realização da etapa |
| NotCan | Number(006,2) | Sim | Nota do candidato |
| CodPar | Number(003,0) | Sim | Código do parecer |

---

## Chave Primária

- AnoCon
- NumCon
- NumEmp
- TipCol
- NumCad
- CodEta

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R121CIE_001

**Tabela:** R121CON

| Origem | Destino |
|--------|---------|
| AnoCon | AnoCon |
| NumCon | NumCon |

### IR_R121CIE_005

**Tabela:** R114ETA

| Origem | Destino |
|--------|---------|
| CodEta | CodEta |

