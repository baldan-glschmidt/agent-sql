# E095EED

## Descrição

Cadastros - Fornecedores - Recibo de Pagamento Autônomo de Terceiros

---

## Resumo

- Campos: 16
- Chave Primária: 3 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFor | Number(009,0) | Não | Código do fornecedor |
| MesAno | Date | Não | Mês / Ano da retenção do INSS |
| IdeUni | Number(009,0) | Não | Identificador de registro |
| NumRpa | Number(009,0) | Não | Número do Recibo de Pagamento Autônomo de Terceiros |
| TipDoc | Number(001,0) | Não | Tipo do Documento |
| CgcCpf | Number(014,0) | Sim | Número do CNPJ ou CPF |
| DocIde | String(014) | Sim | Número do CNPJ (Alfanumérico) ou CPF |
| VlrRem | Number(015,2) | Sim | Valor da Remuneração Recebida pelo Trabalhador |
| VlrBin | Number(015,2) | Sim | Valor base do INSS |
| VlrIns | Number(015,2) | Sim | Valor do INSS |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodFor
- MesAno
- IdeUni

---

## Índices

### E095EEDIndex2

**Tipo:** Unico

Campos:
- CodFor
- MesAno
- CgcCpf
- DocIde
- NumRpa

### E095EEDIndex3

**Tipo:** Não unico

Campos:
- NumRpa

---

## Relacionamentos

### IR_E095EED_000

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

### IR_E095EED_001

**Tabela:** E095INS

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |
| MesAno | MesAno |

