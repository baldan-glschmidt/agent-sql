# E000MED

## Descrição

Tabelas - Integrações - Unidades de Medida

---

## Resumo

- Campos: 4
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| UniMed | String(003) | Não | Código da unidade de medida |

---

## Chave Primária

- SeqInt

---

## Índices

### E000MEDIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- UniMed

---

## Relacionamentos

### IR_E000MED_001

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

