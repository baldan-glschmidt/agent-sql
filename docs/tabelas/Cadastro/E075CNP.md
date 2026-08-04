# E075CNP

## Descrição

Cadastros - Subprodutos/componentes do produto produzido

---

## Resumo

- Campos: 11
- Chave Primária: 2 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdeCnp | Number(009,0) | Não | Identificador do registro de origem do componente utilizado na produção |
| IdeOpr | Number(009,0) | Não | Identificador do registro de origem por produto/derivação |
| CodCmp | String(014) | Não | Código do Componente |
| CodDer | String(007) | Não | Código da Derivação do Componente |
| TipCmp | String(001) | Não | Tipo Produto |
| QtdUti | Number(015,6) | Sim | Quantidade utilizada para fabricação |
| VlrImp | Number(015,2) | Sim | Valor total de importação |
| NumSep | String(050) | Sim | Série de fabricação do Componente |
| CodLot | String(050) | Sim | Código do lote de fabricação do componente |
| CodDep | String(010) | Sim | Código do depósito |

---

## Chave Primária

- IdeUni
- IdeOpr

---

## Índices

### E075CNPIndice1

**Tipo:** Não unico

Campos:
- IdeOpr

### E075CNPIndice2

**Tipo:** Não unico

Campos:
- IdeCnp

---

## Relacionamentos

### IR_E075CNP_002

**Tabela:** E075OPR

| Origem | Destino |
|--------|---------|
| IdeOpr | IdeUni |

