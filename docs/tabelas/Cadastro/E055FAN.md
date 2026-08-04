# E055FAN

## Descrição

Tributos - Alíquota nominal e dedução por faixa de faturamento do simples

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdeTan | Number(009,0) | Não | Tabela Alq. Nom. simples por estado |
| VlrLim | Number(015,2) | Sim | Valor limite de faturamento |
| AlqNom | Number(008,5) | Sim | % Alíquota nominal |
| VlrDed | Number(015,2) | Sim | Valor de dedução |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E055FANIndice1

**Tipo:** Não unico

Campos:
- IdeTan

---

## Relacionamentos

### IR_E055FAN_001

**Tabela:** E055TAN

| Origem | Destino |
|--------|---------|
| IdeTan | IdeUni |

