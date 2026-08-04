# E020PAR

## Descrição

Tabelas - Séries de Notas Fiscais - Parcelas

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da Série da Nota Fiscal |
| CodPar | Number(003,0) | Não | Código sequencial da parcela do título a ser gerado |
| DesPar | String(004) | Não | Descrição da parcela a ser agregada ao número do título |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- CodPar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E020PAR_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

