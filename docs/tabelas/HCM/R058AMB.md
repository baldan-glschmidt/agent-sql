# R058AMB

## Descrição

Ambiente da Planta

---

## Resumo

- Campos: 12
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPlt | Number(005,0) | Não | Código do Site |
| NumAmb | Number(009,0) | Não | Ambiente da Planta |
| DesAmb | String(060) | Sim | Descrição do Ambiente |
| MapSet | Image | Sim | Mapa do Ambiente |
| CatAmb | Number(001,0) | Sim | Categoria do Ambiente |
| CodHvi | Number(003,0) | Sim | Código do Horário de Visita |
| CodPrm | Number(005,0) | Sim | Permissão de Acesso da Visita do Paciente |
| NivAce | Number(002,0) | Sim | Nível de Acesso do Coletor p/ Controle Anti-Dupla |
| QtdPes | Number(004,0) | Sim | Quantidade de Pessoas |
| DatCri | Date | Sim | Data Criação do Ambiente |
| DatExt | Date | Sim | Data Extinção do Ambiente |
| ImgMap | Image | Sim | Imagem Mapa de Ambientes |

---

## Chave Primária

- CodPlt
- NumAmb

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058AMB_000

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

