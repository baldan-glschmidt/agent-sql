# R058PRR

## Descrição

Recintos Aduaneiros por Permissão de Acesso

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPrm | Number(005,0) | Não | Código da Permissão |
| VerPlf | Number(003,0) | Não | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Não | Código do Local Físico |

---

## Chave Primária

- CodPrm
- VerPlf
- CodPlf

---

## Índices

### R058PRRIndice1

**Tipo:** Não unico

Campos:
- VerPlf
- CodPlf

---

## Relacionamentos

### IR_R058PRR_000

**Tabela:** R058PRM

| Origem | Destino |
|--------|---------|
| CodPrm | CodPrm |

### IR_R058PRR_002

**Tabela:** R058PLF

| Origem | Destino |
|--------|---------|
| VerPlf | VerPlf |
| CodPlf | CodPlf |

