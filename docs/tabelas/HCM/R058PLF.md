# R058PLF

## Descrição

Plano de Localização Física

---

## Resumo

- Campos: 21
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| VerPlf | Number(003,0) | Não | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Não | Código do Local Físico |
| DesPlf | String(060) | Sim | Descrição do Local Físico |
| CatPlf | Number(002,0) | Sim | Categoria do Local Físico |
| ImgPlf | Image | Sim | Imagem do Local Físico |
| MapSet | Image | Sim | Mapa do Ambiente |
| CodDac | Number(003,0) | Sim | Código da Definição de Acesso |
| PaiPlf | Number(007,0) | Sim | Pai do Local Físico |
| IdtRel | Number(005,0) | Sim | Posição Relativa ao Pai |
| FusGMT | Number(010,0) | Sim | Diferença de Fuso Horário em Minutos em Relação ao GMT |
| IniHve | Date | Sim | Início do Horario de Verão |
| FimHve | Date | Sim | Fim do Horario de Verão |
| QtdPes | Number(004,0) | Sim | Quantidade de Pessoas |
| NivAce | Number(002,0) | Sim | Nível de Acesso do Coletor p/ Controle Anti-Dupla |
| QtdVag | Number(006,0) | Sim | Quantidade de vagas de estacionamento. |
| CodPrm | Number(005,0) | Sim | Permissão de Acesso da Visita do Paciente |
| CodHvi | Number(003,0) | Sim | Código do Horário de Visita |
| EndRlg | String(100) | Sim | Endereço do Local Físico |
| CodRec | Number(015,0) | Sim | Código do Recinto |
| PerAut | Number(001,0) | Sim | Perfil de autenticação a ser utilizado pelo recinto junto ao Portal Siscomex |
| Protcl | String(036) | Sim | Protocolo do evento retornado pela ADE-02 |

---

## Chave Primária

- VerPlf
- CodPlf

---

## Índices

### R058PLFIND_R058PLF_PAIPLF

**Tipo:** Não unico

Campos:
- PaiPlf

---

## Relacionamentos

### IR_R058PLF_000

**Tabela:** R058VPL

| Origem | Destino |
|--------|---------|
| VerPlf | VerPlf |

### IR_R058PLF_006

**Tabela:** R070DAC

| Origem | Destino |
|--------|---------|
| CodDac | CodDac |

