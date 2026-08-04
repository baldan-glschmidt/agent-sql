# E069CPC

## Descrição

Tabelas - Seguros - Coeficientes por plano e cobertura

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdeCcs | Number(009,0) | Não | Identificador da cobertura de seguro |
| IdePse | Number(009,0) | Não | Identificador do registro de plano do seguro |
| CoeCob | Number(009,8) | Sim | Coeficiente sobre a cobertura |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E069CPCIndice2

**Tipo:** Não unico

Campos:
- IdePse

### E069CPCIndice3

**Tipo:** Não unico

Campos:
- IdeCcs

---

## Relacionamentos

### IR_E069CPC_001

**Tabela:** E069CCS

| Origem | Destino |
|--------|---------|
| IdeCcs | IdeUni |

### IR_E069CPC_002

**Tabela:** E069PSE

| Origem | Destino |
|--------|---------|
| IdePse | IdeUni |

