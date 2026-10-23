# R058LCD

## Descrição

Cadastro Comandos por Lote de Comandos de Acesso

---

## Resumo

- Campos: 7
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodLcm | Number(003,0) | Não | Código do Lote do Acesso |
| SeqExe | Number(003,0) | Não | Sequência da Execução |
| CodPlt | Number(005,0) | Sim | Código do Site |
| CodRlg | Number(005,0) | Sim | Código do Coletor |
| CodCmd | Number(003,0) | Sim | Código do Comando |
| ParCmd | String(015) | Sim | Parâmetro do Comando |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |

---

## Chave Primária

- CodLcm
- SeqExe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058LCD_000

**Tabela:** R058LCM

| Origem | Destino |
|--------|---------|
| CodLcm | CodLcm |

### IR_R058LCD_002

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R058LCD_003

**Tabela:** R058RLG

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodRlg | CodRlg |

