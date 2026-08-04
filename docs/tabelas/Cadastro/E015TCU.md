# E015TCU

## Descrição

Cadastros - Unidades de Medida - Conversões

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| UniMed | String(003) | Não | Unidade de medida da quantidade a ser convertida |
| UniMe2 | String(003) | Não | Unidade de medida para qual a quantidade será convertida |
| TipCnv | String(001) | Não | Operação de multiplicação (*) ou divisão (/) a ser utilizada na conversão |
| VlrCnv | Number(013,6) | Não | Valor para converter a "1ª Unidade Medida" para "2ª Unidade Medida" |
| CodReg | Number(004,0) | Sim | Código da regra p/ formar conversão de uma Unidade Medida não atendidas pela conversão convencional |

---

## Chave Primária

- UniMed
- UniMe2

---

## Índices

### E015TCUIndice1

**Tipo:** Não unico

Campos:
- UniMe2

---

## Relacionamentos

### IR_E015TCU_000

**Tabela:** E015MED

| Origem | Destino |
|--------|---------|
| UniMed | UniMed |

### IR_E015TCU_001

**Tabela:** E015MED

| Origem | Destino |
|--------|---------|
| UniMe2 | UniMed |

