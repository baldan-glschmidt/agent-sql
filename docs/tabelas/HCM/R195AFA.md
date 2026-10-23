# R195AFA

## Descrição

Cenário - Histórico de Afastamento

---

## Resumo

- Campos: 11
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatAfa | Date | Não | Data do Afastamento |
| HorAfa | Number(005,0) | Não | Hora do Afastamento |
| DatTer | Date | Sim | Data do Término do Afastamento |
| HorTer | Number(005,0) | Sim | Hora do Término do Afastamento |
| SitAfa | Number(003,0) | Sim | Situação de Afastamento |
| CauDem | Number(002,0) | Sim | Causa Demissão do Colaborador |
| AtuQua | Number(001,0) | Sim | Define se o quadro de vagas foi atualizado ou não após gerar um afastamento de demissão |

---

## Chave Primária

- NumEmp
- CodCen
- TipCol
- NumCad
- DatAfa
- HorAfa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R195AFA_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

### IR_R195AFA_008

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| SitAfa | CodSit |

