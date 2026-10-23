# R234EVN

## Descrição

Administração de Eventos

---

## Resumo

- Campos: 40
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEvn | Number(009,0) | Não | Código do Evento |
| NomEvn | String(200) | Sim | Nome do Evento |
| IdeEvn | String(030) | Sim | Identificador do evento |
| CatEvn | Number(003,0) | Sim | Categoria do Evento |
| CodCua | Number(009,0) | Sim | Código do Curso de Aperfeiçoamento |
| ConFre | Number(001,0) | Sim | Define a forma de controlar a frequência do participante |
| DatIni | Date | Sim | Data de Início do Evento |
| DatFim | Date | Sim | Data de Término do Evento |
| DatIIn | Date | Sim | Início das inscrições de participantes no evento |
| DatFIn | Date | Sim | Prazo para inscrições de participantes no evento |
| QtdAul | Number(003,0) | Sim | Quantidade de Aulas |
| CarHor | Number(010,0) | Sim | Carga Horária |
| CodUsu | Number(010,0) | Sim | Identificação do Coordenador do Evento |
| CodFes | Number(008,0) | Sim | Código da Entidade |
| QtdVag | Number(006,0) | Sim | Quantidade de Vagas |
| TipRea | Number(003,0) | Sim | Tipo de Realização |
| DivEvn | Number(001,0) | Sim | Divulgar Evento |
| DvgWEB | String(001) | Sim | Divulga o Evento na WEB |
| PerIns | Number(001,0) | Sim | Define a restrição aplicada na tela de manutenção de participantes do evento |
| SitEvn | Number(001,0) | Sim | Tipo da Situação do Evento |
| DatCan | Date | Sim | Data de cancelamento do evento |
| CodMoc | Number(003,0) | Sim | Motivo de cancelamento do evento |
| DesCon | String(8001) | Sim | Descrição do Conteúdo |
| DesObu | String(2000) | Sim | Descrição do Objetivo |
| MetCua | String(1000) | Sim | Metodologia Curso |
| PubAlv | String(400) | Sim | Público Alvo |
| ObsCoo | String(400) | Sim | Observações do coordenador do evento |
| FreCua | Number(005,2) | Sim | % de Frequência Mínima no evento |
| MedCua | Number(005,2) | Sim | Média Mínima do Curso |
| CodTst | String(005) | Sim | Código do questionário da avaliação de eficácia |
| IniEfi | Date | Sim | Tempo de observação para liberar a avaliação de eficácia |
| FimEfi | Date | Sim | Data limite para ocorrer a avaliação de eficácia |
| AvaRea | String(001) | Sim | Indica se possui Avaliação de Reação |
| AvRWeb | String(001) | Sim | Indica se a avaliação de reação poderá ser feita via WEB |
| IniRea | Date | Sim | Data que será liberada a avaliação de reação |
| FimRea | Date | Sim | Data limite para ocorrer a avaliação de reação |
| AvrAno | String(001) | Sim | Permitir transformar uma avaliação de reação identificada em anônima |
| CriRep | Number(001,0) | Sim | Define se a reprovação será por média ou frequencia quando ambas estiverem abaixo do mínimo |
| MetEfi | Number(003,0) | Sim | Percentual mínimo para o evento ser considerado eficaz |
| TipTre | Number(001,0) | Sim | Tipo do treinamento/capacitação |

---

## Chave Primária

- CodEvn

---

## Índices

### R234EVNIndice1

**Tipo:** Unico

Campos:
- IdeEvn

---

## Relacionamentos

### IR_R234EVN_003

**Tabela:** R233CAT

| Origem | Destino |
|--------|---------|
| CatEvn | CatEvn |

### IR_R234EVN_015

**Tabela:** R140REA

| Origem | Destino |
|--------|---------|
| TipRea | TipRea |

