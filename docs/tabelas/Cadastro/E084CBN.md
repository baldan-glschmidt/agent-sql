# E084CBN

## Descrição

Cadastros - Combinações da Máscara Produto

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Empresa |
| CodMpr | String(008) | Não | Código da Máscara |
| CodCpr | String(014) | Não | Código do Componente da Máscara de Produto |
| SeqCbn | Number(004,0) | Não | Número  Sequencial  das combinações |
| CodMpc | String(008) | Não | Código da Opção da Máscara de Produto |
| CodCpc | String(014) | Não | Código do Componente da Opção da Máscara de Produto |
| CodUsu | Number(010,0) | Não | Código do Usuário que alterou |
| DatGer | Date | Não | Data Geração ou Alteração da ligação |
| HorGer | Number(005,0) | Não | Hora da geração/última alteração do registro |

---

## Chave Primária

- CodEmp
- CodMpr
- CodCpr
- SeqCbn

---

## Índices

### E084CBNIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodMpc
- CodCpc

---

## Relacionamentos

### IR_E084CBN_001

**Tabela:** E084MPR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMpr | CodMpr |

### IR_E084CBN_002

**Tabela:** E084CPR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMpr | CodMpr |
| CodCpr | CodCpr |

### IR_E084CBN_004

**Tabela:** E084MPC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMpc | CodMpc |

### IR_E084CBN_005

**Tabela:** E084CPC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMpc | CodMpc |
| CodCpc | CodCpc |

