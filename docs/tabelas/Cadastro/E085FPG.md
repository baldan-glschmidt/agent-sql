# E085FPG

## Descrição

Cadastros - Clientes - Formas de Pagamento

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCli | Number(009,0) | Não | Código do Cliente |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFpg | Number(002,0) | Não | Código da forma de pagamento |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |

---

## Chave Primária

- CodCli
- CodEmp
- CodFil
- CodFpg

---

## Índices

### E085FPGIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFpg

---

## Relacionamentos

### IR_E085FPG_003

**Tabela:** E066FPG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFpg | CodFpg |

