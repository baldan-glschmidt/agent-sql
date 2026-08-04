# E070ENT

## Descrição

Cadastros - Empresas - Endereços de Entrega

---

## Resumo

- Campos: 18
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| SeqEnt | Number(005,0) | Não | Sequencia do endereço de entrega |
| EndEnt | String(100) | Não | Endereço de entrega |
| CplEnt | String(200) | Sim | Complemento do endereço de entrega |
| CepEnt | Number(008,0) | Não | CEP do endereço de entrega |
| BaiEnt | String(075) | Sim | Bairro do endereço de entrega |
| CidEnt | String(060) | Não | Cidade do endereço de entrega |
| EstEnt | String(002) | Não | Estado do endereço de entrega |
| PaiEnt | String(004) | Sim | Código do país de entrega |
| SitReg | String(001) | Não | Situação do registro |
| UsuGer | Number(010,0) | Sim | Código do usuário responsável pelo geração do registro |
| HorGer | Number(005,0) | Sim | Hora do cadastro do registro |
| DatGer | Date | Sim | Data do cadastro do registro |
| UsuAlt | Number(010,0) | Sim | Código do usuário responsável pelo alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| NumEnt | String(060) | Sim | Número do endereço de entrega |

---

## Chave Primária

- CodEmp
- CodFil
- SeqEnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E070ENT_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

