# R040PRC

## Descrição

Cadastro de Programação de Férias Coletivas

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| PrgDat | Date | Não | Data Início - Programação |
| PrgDfe | Number(004,2) | Sim | Dias Férias - Programação |
| PrgDab | Number(004,2) | Sim | Dias Abono - Programação |
| Prg13s | String(001) | Sim | Pagar 13° Salário - Programação |
| PrgDpg | Date | Sim | Data Pagto - Programação |
| GerAdt | String(001) | Sim | Gerar Adiantamento na Programação |
| PrgPcl | Number(002,0) | Sim | Número de Parcelas de Desconto - Programação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- PrgDat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
