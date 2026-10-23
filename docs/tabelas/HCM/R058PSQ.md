# R058PSQ

## Descrição

Respostas da Pesquisa de Satisfação

---

## Resumo

- Campos: 11
- Chave Primária: 0 campo(s)
- Índices: 0
- Relacionamentos: 5

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTaa | Number(009,0) | Sim | Código do Dispositivo |
| CodPer | Number(004,0) | Não | Código da pergunta da pesquisa de satisfação |
| CodRes | Number(004,0) | Não | Código da opção de resposta da pergunta de pesquisa de satisfação |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador |
| TipDoc | Number(001,0) | Sim | Tipo do Documento do Visitante |
| NumDoc | String(020) | Sim | Número do Documento do Visitante |
| DatPsq | Date | Não | Data da resposta da pesquisa |
| HorPsq | Number(005,0) | Não | Hora da resposta da pesquisa |
| NumCra | Number(012,0) | Sim | Número do crachá |

---

## Chave Primária

Não possui.

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058PSQ_000

**Tabela:** R058DSP

| Origem | Destino |
|--------|---------|
| CodTaa | CodDsp |

### IR_R058PSQ_001

**Tabela:** R058PER

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |

### IR_R058PSQ_002

**Tabela:** R058RES

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |
| CodRes | CodRes |

### IR_R058PSQ_005

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R058PSQ_007

**Tabela:** R090VIS

| Origem | Destino |
|--------|---------|
| TipDoc | TipDoc |
| NumDoc | NumDoc |

