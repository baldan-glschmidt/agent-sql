# E075NFC

## Descrição

Cadastros - Notas Fiscais de Compra dos Componentes

---

## Resumo

- Campos: 12
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdeOpr | Number(009,0) | Não | Identificador do registro de origem por produto/derivação |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do Fornecedor |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| SeqIpc | Number(003,0) | Não | Sequência do item na nota fiscal de entrada |
| CodCmp | String(014) | Não | Código do Componente |
| CodDer | String(007) | Não | Código da Derivação do Componente |
| NumSep | String(050) | Sim | Série de fabricação do Componente |
| CodLot | String(050) | Sim | Código do lote de fabricação do componente |
| CodDep | String(010) | Sim | Código do depósito |

---

## Chave Primária

- IdeUni
- IdeOpr

---

## Índices

### E075NFCIndice1

**Tipo:** Não unico

Campos:
- IdeOpr

---

## Relacionamentos

### IR_E075NFC_001

**Tabela:** E075OPR

| Origem | Destino |
|--------|---------|
| IdeOpr | IdeUni |

