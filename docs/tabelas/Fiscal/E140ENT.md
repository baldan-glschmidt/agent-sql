# E140ENT

## Descrição

Vendas - Controle de entregas

---

## Resumo

- Campos: 21
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqEnt | Number(004,0) | Não | Sequência do registro de entrega |
| StaEnt | String(001) | Não | Status da entrega |
| DatEnt | Date | Sim | Data da entrega |
| HorEnt | Number(005,0) | Sim | Hora da entrega |
| CodTra | Number(009,0) | Sim | Código da Transportadora |
| PlaVei | String(010) | Sim | Placa do veículo |
| ResRec | String(254) | Sim | Nome do responsável pelo recebimento |
| TipDoc | String(004) | Sim | Tipo de documento apresentado pelo recebedor |
| DocEnt | String(099) | Sim | Número do documento apresentado no ato da entrega da mercadoria |
| LatEnt | String(049) | Sim | Latitude da entrega |
| LonEnt | String(049) | Sim | Longitude da entrega |
| ObsEnt | String(999) | Sim | Observação sobre a entrega |
| ImaEnt | String(999) | Sim | Imagem do comprovante de entrega |
| DatGer | Date | Não | Data da geração do registro |
| HorGer | Number(005,0) | Não | Hora da geração do registro |
| UsuGer | Number(010,0) | Não | Usuário responsável pela geração do registro |
| ImaBlb | Image | Sim | Imagem a ser utilizada para o comprovante de entrega |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqEnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140ENT_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

