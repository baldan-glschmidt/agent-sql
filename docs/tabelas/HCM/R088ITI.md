# R088ITI

## Descrição

Cadastro de Itinerários de Táxis

---

## Resumo

- Campos: 17
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPlt | Number(005,0) | Não | Código do Site |
| CodIti | Number(004,0) | Não | Código do Itinerário |
| DesIti | String(030) | Sim | Descrição do Itinerário |
| CidOri | Number(007,0) | Sim | Código da Cidade de Origem |
| EndOri | String(050) | Sim | Endereço de Origem |
| BaiOri | Number(004,0) | Sim | Bairro de Origem |
| CepOri | Number(008,0) | Sim | CEP de Origem |
| CidDes | Number(007,0) | Sim | Código da Cidade de Destino |
| EndDes | String(050) | Sim | Endereço de Destino |
| BaiDes | Number(004,0) | Sim | Bairro de Destino |
| CepDes | Number(008,0) | Sim | CEP de Destino |
| TemPre | Number(010,0) | Sim | Tempo Previsto da Viagem |
| TipIti | Number(001,0) | Sim | Tipo de Itinerário de Táxi |
| QuiIti | Number(007,0) | Sim | Quilometragem do Trajeto Itinerário |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou a Entrada |
| DatUsu | Date | Sim | Data da Alteração pelo Usuário |
| HorUsu | Number(005,0) | Sim | Hora da Alteração pelo Usuário |

---

## Chave Primária

- CodPlt
- CodIti

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088ITI_000

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

