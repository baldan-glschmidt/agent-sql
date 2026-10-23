# R038CSA

## Descrição

Histórico de Composição Salarial

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CmpAlt | Date | Não | Competência de Alteração |
| CodMot | Number(003,0) | Sim | Código Motivo Alteração |
| ValSal | Number(013,4) | Sim | Valor do Salário |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R038CSA_004

**Tabela:** R076MOT

| Origem | Destino |
|--------|---------|
| CodMot | CodMot |

