# E075VIN

## Descrição

Cadastros - Vendas para o mercado interno

---

## Resumo

- Campos: 11
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdeOpr | Number(009,0) | Não | Identificador do registro de origem por produto/derivação |
| CodTpr | String(004) | Não | Código da tabela de preço |
| DatIni | Date | Não | Data de Inicio da Tabela de Preço |
| CodMod | String(014) | Não | Código do Modelo |
| CodFxa | String(015) | Não | Código da Faixa da Grade |
| CodFil | Number(005,0) | Não | Código da filial |
| CodCli | Number(009,0) | Não | Código do Cliente |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| SeqInv | Number(003,0) | Não | Sequência do item na nota fiscal de saída |

---

## Chave Primária

- IdeUni
- IdeOpr

---

## Índices

### E075VINIndice1

**Tipo:** Não unico

Campos:
- IdeOpr

---

## Relacionamentos

### IR_E075VIN_001

**Tabela:** E075OPR

| Origem | Destino |
|--------|---------|
| IdeOpr | IdeUni |

